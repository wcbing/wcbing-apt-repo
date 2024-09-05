import requests
import re
from module.merge_deb import merge_latest_deb

deb_repo = "https://download.sublimetext.com/"

deb_Packages_url = deb_repo + "apt/stable/Packages"
deb_Packages = requests.get(deb_Packages_url).text
debs = re.split("(?=Package: )", deb_Packages)[1:]
# print(debs)

# sublime 的 Packages 按照版本升序排列，倒数两个为 amd64 和 arm64 最新版本

sublime_text_debs = []
sublime_merge_debs = []

for deb in debs:
    if "Package: sublime-text\n" in deb:
        sublime_text_debs.append(deb)
    elif "Package: sublime-merge\n" in deb:
        sublime_merge_debs.append(deb)

deb_latest = (
    sublime_text_debs[-2]
    + sublime_text_debs[-1]
    + sublime_merge_debs[-2]
    + sublime_merge_debs[-1]
)

merge_latest_deb("sublime", deb_repo, deb_latest)
