#!/usr/bin/env python3

import argparse
import gzip
import io
import json
import logging
import lzma
import os
import re
import requests
import sys
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

package_version = {arch: {} for arch in ["all", "amd64", "i386", "arm64"]}
package_info = {arch: {} for arch in ["all", "amd64", "i386", "arm64"]}
lock = {arch: Lock() for arch in ["all", "amd64", "i386", "arm64"]}

USER_AGENT = "Debian APT-HTTP/1.3 (2.6.1)"  # from Debian 12

"""
repo info json format:
"repo_name": {     
    "repo": repo url, end with "/"
    "xxx_path": {
        "arch": repo Packages file path of "arch", start with no "/"
    }
}
"""


def read_repo_list(repo_list_file: str) -> dict:
    try:
        with open(repo_list_file, "r") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error reading repo list: {e}")
        return {}


def get_remote_packages(repo_url: str, file_path: str) -> bytes:
    """
    get the packages file content from remote repo
    """
    file_url = repo_url + file_path
    try:
        response = requests.get(
            file_url, timeout=10, headers={"User-Agent": USER_AGENT}
        )
        if response.status_code != 200:
            logging.error(
                f"GetError: {file_url} returned status {response.status_code}"
            )
            return b""

        content = b""
        if file_url.endswith(".gz"):  # Packages.gz
            with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as f:
                content = f.read()
        elif file_url.endswith(".xz"):  # Packages.xz
            with lzma.LZMAFile(io.BytesIO(response.content)) as f:
                content = f.read()
        else:  # Packages
            content = response.content

        # complete the two newlines if the ending is less than two newlines
        # 结尾不足两个换行符的话，补全两个换行符
        if not content.endswith(b"\n\n"):
            content += b"\n"
        return content.replace(b"Filename: ", f"Filename: {repo_url}".encode())
    except Exception as e:
        logging.error(f"Error fetching packages: {e}")
        return b""


def get_latest(deb_packages: bytes):
    """
    split the information of each packet, deduplication and store the latest in infoList
    将每个包的信息分割开，去重并将最新的存放到 infoList 中
    """
    deb_packages = re.sub(rb"^Package: ", b"{{start}}Package: ", deb_packages, flags=re.MULTILINE)
    info_list = deb_packages.split(b"{{start}}")[1:]

    find_name = re.compile(rb"Package: (.+)")
    find_arch = re.compile(rb"Architecture: (.+)")
    find_version = re.compile(rb"Version: (.+)")

    for v in info_list:
        try:
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
        except Exception as e:
            logging.error(f"Error processing package {name}: {e}")
    return


def process_repo(r: dict):
    """
    获取仓库中不同架构子仓库的内容，最后调用 get_latest 去重并保存。
    """
    try:
        for path in r["path"].values():
            get_latest(get_remote_packages(r["repo"], path))
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
    parser.add_argument("--local", type=str, help="Process Packages in local repo")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    # 处理本地 repo
    if args.local:
        with open(args.local) as f:
            get_latest(f.read().encode())

    # 读取 repo_list 配置
    repo_list = read_repo_list(args.repo)
    if not repo_list:
        sys.exit()

    # 多线程，同时限制最大线程数
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_repo, repo_list.values())

    # 分别输出到不同文件
    for arch in ["amd64", "arm64"]:
        os.makedirs(f"deb/dists/wcbing/main/binary-{arch}/", exist_ok=True)
        with open(f"deb/dists/wcbing/main/binary-{arch}/Packages", "+wb") as f:
            for i in package_info[arch].values():
                f.write(i)
            for i in package_info["all"].values():
                f.write(i)
