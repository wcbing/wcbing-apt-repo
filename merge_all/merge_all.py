import requests
import json


"""
Merge all deb packages info from repos to a Packages file.
These repos only include the latest deb packages.
"""

repo_info_list = []
amd64_Packages_all = ""

# read all repo info from json file
with open("merge_all/repo_info.json", "r") as all_repo_info:
    repo_info_list = json.loads(all_repo_info.read())
all_repo_info.close()

"""
repo info json format:
{
    "name": repo name
    "repo": repo url, end with "/"
    "Packages_path": repo Packages file path, start with no "/"
}
"""

# get deb packages info from repo
for i in repo_info_list:
    # get amd64 deb packages info
    if "amd64_path" in i:
        amd64_Packages_info = requests.get(i["repo"] + i["amd64_path"]).text
        amd64_Packages_all += amd64_Packages_info.replace(
            "Filename: ", "Filename: " + i["repo"]
        )
        print(i["name"] + " x64 repo: done")

# write deb packages info to local Packages file
with open("deb/Packages", "a+") as f:
    f.write(amd64_Packages_all)
f.close()
