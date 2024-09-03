import requests
from module.check import deb

release_url = "https://github.com/clash-verge-rev/clash-verge-rev/releases"

latest_req = requests.head(release_url + "/latest")
vversion = latest_req.headers["Location"].split("/")[-1]  # v1.1.1
version = vversion[1:]  # 1.1.1
# print(vversion, version)

# /v1.7.5/clash-verge_1.7.5_amd64.deb
x64_deb_url = (
    release_url + "/download/" + vversion + "/clash-verge_" + version + "_amd64.deb"
)

deb("clash-verge", version, x64_deb_url)
