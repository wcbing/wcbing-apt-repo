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
    repo = i["repo"]
    release_url = f"https://github.com/{repo}/releases/"
    latest_req = requests.head(release_url + "latest")
    version_tag = latest_req.headers["Location"].split("/")[-1]  # v1.1.1
    stripped_version = version_tag[1:]  # 1.1.1
    x64_deb_name = i["x64_deb_name"].format(version_tag=version_tag, stripped_version=stripped_version)
    x64_deb_url = release_url + "download/" + x64_deb_name

    deb(i["name"], version_tag, x64_deb_url)
