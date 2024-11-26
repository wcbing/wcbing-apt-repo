#!/usr/bin/env python3

import argparse
import json
import logging
import os
import re
import requests
import sys
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

config = {}
package_version = {"all": {}, "amd64": {}, "i386": {}, "arm64": {}}
package_info = {"all": {}, "amd64": {}, "i386": {}, "arm64": {}}
lock = {"all": Lock(), "amd64": Lock(), "i386": Lock(), "arm64": Lock()}

"""
repo info json format:
{
    "name": repo name
    "only_latest": only has the latest version or not
    "repo": repo url, end with "/"
    "xxx_path": repo xxx Packages file path, start with no "/"
}
"""


def read_repo_list(repo_list_file):
    try:
        with open(repo_list_file, "r") as f:
            return json.load(f)
    except Exception as e:
        logging.warning(f"Error reading repo list: {e}")
        return []


# get the packages file content from remote repo
def get_remote_packages(repo_url, file_path):
    file_url = repo_url + file_path
    try:
        response = requests.get(file_url, timeout=10)
        if response.status_code != 200:
            logging.warning(
                f"GetError: {file_url} returned status {response.status_code}"
            )
            return b""
        content = response.content
        # complete the two newlines if the ending is less than two newlines
        # 结尾不足两个换行符的话，补全两个换行符
        if not content.endswith(b"\n\n"):
            content += b"\n"
        return content.replace(b"Filename: ", f"Filename: {repo_url}".encode())
    except Exception as e:
        logging.warning(f"Error fetching packages: {e}")
        return b""


def get_latest(deb_packages):
    # divide the information of each packet, store it in infoList
    # 将每个包的信息分割开，存放到 infoList 中
    deb_packages = deb_packages.replace(b"Package: ", b"{{start}}Package: ")
    info_list = deb_packages.split(b"{{start}}")[1:]

    find_name = re.compile(rb"Package: (.+)")
    find_arch = re.compile(rb"Architecture: (.+)")
    find_version = re.compile(rb"Version: (.+)")

    for v in info_list:
        name = find_name.search(v).group(1).decode()
        arch = find_arch.search(v).group(1).decode()
        tmp_version = find_version.search(v).group(1).decode()
        with lock[arch]:
            if (
                name not in package_version[arch]
                or os.system(
                    f"dpkg --compare-versions {tmp_version} gt {package_version[arch][name]}"
                )
                == 0
            ):
                package_version[arch][name] = tmp_version
                package_info[arch][name] = v
    return


def process_repo(r):
    try:
        deb_packages = b""
        if r.get("amd64_path"):
            # 获取 Repo 中 Amd64 包信息
            deb_packages += get_remote_packages(r["repo"], r["amd64_path"])
        if r.get("arm64_path"):
            # 获取 Repo 中 Arm64 包信息
            deb_packages += get_remote_packages(r["repo"], r["arm64_path"])
        if r.get("mix_path"):
            # 获取扁平 Repo 中包信息
            deb_packages += get_remote_packages(r["repo"], r["mix_path"])
        get_latest(deb_packages)
    except Exception as e:
        logging.error(f"Error processing repo {r.get('name', 'unknown')}: {e}")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="A script to merge the latest versions Packages files"
    )
    parser.add_argument(
        "-r",
        "--repo",
        type=str,
        default="data/repo_list.json",
        help="Path to the repository list file. Default is 'data/repo_list.json'.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    repo_list = args.repo
    repo_list = read_repo_list(repo_list)
    if not repo_list:
        sys.exit()
    # 多线程，同时限制最大线程数
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_repo, repo_list)

    # 有需要可以分别输出到不同文件
    for list in package_info.values():
        for i in list.values():
            print(i.decode(), end="")
