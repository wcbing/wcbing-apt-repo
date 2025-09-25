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
import apt_pkg
from apt_pkg import version_compare

apt_pkg.init()  # 初始化 apt_pkg

arch_List = ["amd64", "arm64", "all", "i386"]
packages = {arch: {} for arch in arch_List} # 存放用于生成 Packages 的内容
""" packages format:
{
    "arch": {
        "package1": {
            "version": "1.0.0",
            "package": ""
        }
    }
}
"""
lock = {arch: Lock() for arch in arch_List}

USER_AGENT = "Debian APT-HTTP/1.3 (3.0.3)"  # from Debian 13

def read_repo_list(repo_list_file: str) -> dict:
    """
    repo info json format:
    "repo_name": {
        "repo": repo url, end with "/" is better
        "path": {
            "arch": repo Packages file path of "arch", don't start with "/"
        }
    }
    """
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
    file_url = os.path.join(repo_url, file_path)
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


def split_latest(packages_file_content: bytes):
    """
    split the information of each packet, deduplication and store the latest in infoList
    将每个包的信息分割开，去重并将最新的存放到 infoList 中
    """
    packages_file_content = re.sub(
        rb"^Package: ", b"{{start}}Package: ", packages_file_content, flags=re.MULTILINE
    )
    package_list = packages_file_content.split(b"{{start}}")[1:]

    find_name = re.compile(rb"Package: (.+)")
    find_arch = re.compile(rb"Architecture: (.+)")
    find_version = re.compile(rb"Version: (.+)")

    for package in package_list:
        name = "unknown"
        try:
            name = find_name.search(package).group(1).decode()
            arch = find_arch.search(package).group(1).decode()
            tmp_version = find_version.search(package).group(1).decode()
            with lock[arch]:
                # 使用 apt_pkg 进行版本比较
                if (
                    name not in packages[arch]
                    or version_compare(tmp_version, packages[arch][name]["version"]) > 0
                ):
                    packages[arch][name] = {"package": package, "version": tmp_version}
        except Exception as e:
            logging.error(f"Error processing package {name}: {e}")
    return


def process_repo(r: dict):
    """
    获取仓库中不同架构子仓库的内容，最后调用 get_latest 去重并保存。
    """
    try:
        for path in r["path"].values():
            split_latest(get_remote_packages(r["repo"], path))
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
            split_latest(f.read().encode())

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
            for i in packages[arch].values():
                f.write(i["package"])
            for i in packages["all"].values():
                f.write(i["package"])
