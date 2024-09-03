import requests
from module.check import deb

release_url = "https://github.com/chen08209/FlClash/releases"

latest_req = requests.head(release_url + "/latest")
vversion = latest_req.headers["Location"].split("/")[-1]  # v1.1.1
version = vversion[1:]  # 1.1.1
# print(vversion, version)

# /v0.8.54/FlClash-0.8.54-linux-amd64.deb
x64_deb_url = (
    release_url + "/download/" + vversion + "/FlClash-" + version + "-linux-amd64.deb"
)

deb("flclash", version, x64_deb_url)
