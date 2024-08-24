import requests
from module.check import deb

name = "flclash"

release_url = "https://github.com/chen08209/FlClash/releases"

res = requests.head(release_url + "/latest", allow_redirects=False)
vversion = requests.Session().get_redirect_target(res).split("/")[-1]  # v1.1.1
version = vversion[1:]  # 1.1.1
# print(vversion, version)

# /v0.8.54/FlClash-0.8.54-linux-amd64.deb
x64_deb_url = (
    release_url + "/download/" + vversion + "/FlClash-" + version + "-linux-amd64.deb"
)

deb(name, version, x64_deb_url)
