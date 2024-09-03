import requests
from module.check import deb

release_url = "https://github.com/obsidianmd/obsidian-releases/releases"

latest_req = requests.head(release_url + "/latest")
vversion = latest_req.headers["Location"].split("/")[-1]  # v1.1.1
version = vversion[1:]  # 1.1.1
# print(vversion, version)

# /v1.6.7/obsidian_1.6.7_amd64.deb
x64_deb_url = (
    release_url + "/download/" + vversion + "/obsidian_" + version + "_amd64.deb"
)

deb("obsidian", version, x64_deb_url)
