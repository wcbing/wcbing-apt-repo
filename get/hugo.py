import requests
from module.check import deb

release_url = "https://github.com/gohugoio/hugo/releases"

latest_req = requests.head(release_url + "/latest")
vversion = latest_req.headers["Location"].split("/")[-1]  # v1.1.1
version = vversion[1:]  # 1.1.1
# print(vversion, version)

# /v0.129.0/hugo_0.129.0_linux-amd64.deb
x64_deb_url = (
    release_url + "/download/" + vversion + "/hugo_" + version + "_linux-amd64.deb"
)

deb("hugo", version, x64_deb_url)
