import requests
from module.check import check_download

name = "mihomo"

release_url = "https://github.com/MetaCubeX/mihomo/releases"

res = requests.head(release_url + "/latest", allow_redirects=False)
vversion = requests.Session().get_redirect_target(res).split("/")[-1]  # v1.1.1
version = vversion[1:]  # 1.1.1
# print(vversion, version)

# /v1.18.6/mihomo-linux-amd64-compatible-v1.18.6.deb
x64_deb_url = (
    release_url + "/download/" + vversion + "/"
    + name + "-linux-amd64-compatible-" + vversion + ".deb"
)

check_download(name, version, x64_deb_url)
