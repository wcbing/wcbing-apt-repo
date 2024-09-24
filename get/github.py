import requests
import json
from module.check import deb

github_info_list = []

# read all repo info from json file
with open("get/github.json", "r") as all_repo_info:
    github_info_list = json.loads(all_repo_info.read())
all_repo_info.close()

"""
repo info json format:
{
    "name": name
    "repo": repo
    "x64_deb_name": x86 deb file name
}
"""

# get version info from repo
for i in github_info_list:
    release_url = f"https://github.com/{i["repo"]}/releases/"
    latest_req = requests.head(release_url + "latest")
    vversion = latest_req.headers["Location"].split("/")[-1]  # v1.1.1
    version = vversion[1:]  # 1.1.1
    x64_deb_name = i["x64_deb_name"].format(vversion=vversion, version=version)
    x64_deb_url = release_url + "download/" + x64_deb_name

    deb(i["name"], vversion, x64_deb_url)
