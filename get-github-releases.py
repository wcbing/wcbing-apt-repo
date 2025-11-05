#!/usr/bin/env python3
import argparse
import requests
import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, wait
from check_downloader import check_download

git_repo_list = {}

CONFIG = {"data_dir": "data", "proxy": "", "thread": 5}


# 读取命令行参数
def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", default="data", help="从 <DATA> 读取仓库配置")
    parser.add_argument(
        "-p", "--proxy", default="", help="Github 代理"
    )
    parser.add_argument(
        "-t", "--thread", type=int, default=5, help="并发下载线程数量，默认为 5"
    )
    args = parser.parse_args()
    CONFIG.update({"data_dir": args.data, "proxy": args.proxy, "thread": args.thread})


if __name__ == "__main__":
    read_args()

    # read all repo info 读取所有仓库配置
    with open(os.path.join(CONFIG["data_dir"], "github.json"), "r") as f:
        git_repo_list = json.load(f)

    tasks = []
    with ThreadPoolExecutor(max_workers=CONFIG["thread"]) as executor:
        for name, repo in git_repo_list.items():
            if "site" in repo:
                repo_url = os.path.join(repo["site"], repo['repo'])
            else:
                # 默认认为是 GitHub 仓库地址，同时使用代理
                repo_url = os.path.join(CONFIG["proxy"], "https://github.com", repo["repo"])
            # get latest releases tag 获取最新版本标签
            location = requests.head(repo_url + "/releases/latest").headers.get("Location", "")
            match = re.search(r".*releases/tag/(.*)", location)
            if not match:
                continue
            releases_tag = match.group(1)
            version = match.group() if (match := re.search("[0-9][^_]*", releases_tag)) else ""


            for arch, file_name in repo["file_list"].items():
                release_file = file_name.format(
                    releases_tag=releases_tag, version=version
                )
                file_url = f"{repo_url}/releases/download/{releases_tag}/{release_file}"
                # 提交任务到线程池
                tasks.append(
                    executor.submit(check_download, name, version, file_url, arch)
                )
        # 等待所有任务完成
        wait(tasks)
