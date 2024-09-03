import requests
from module.check import deb

release_url = "https://github.com/MetaCubeX/mihomo/releases"

latest_req = requests.head(release_url + "/latest")
vversion = latest_req.headers["Location"].split("/")[-1]  # v1.1.1
version = vversion[1:]  # 1.1.1
# print(vversion, version)

# /v1.18.6/mihomo-linux-amd64-compatible-v1.18.6.deb
x64_deb_url = (
    release_url + "/download/" + vversion + "/mihomo-linux-amd64-compatible-" + vversion + ".deb"
)

deb("mihomo", version, x64_deb_url)
