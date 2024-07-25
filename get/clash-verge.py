import requests
from module.check import check_download

name = "clash-verge"

release_url = "https://github.com/clash-verge-rev/clash-verge-rev/releases"

res = requests.head(release_url + "/latest", allow_redirects=False)
vversion = requests.Session().get_redirect_target(res).split("/")[-1]  # v1.1.1
version = vversion[1:]  # 1.1.1
# print(vversion, version)

# /v1.7.5/clash-verge_1.7.5_amd64.deb
x64_deb_url = (
    release_url + "/download/" + vversion + "/" + name + "_" + version + "_amd64.deb"
)

check_download(name, version, x64_deb_url)
