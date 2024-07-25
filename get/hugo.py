import requests
from module.check import check_download

name = "hugo"

release_url = "https://github.com/gohugoio/hugo/releases"

res = requests.head(release_url + "/latest", allow_redirects=False)
vversion = requests.Session().get_redirect_target(res).split("/")[-1]  # v1.1.1
version = vversion[1:]  # 1.1.1
# print(vversion, version)

# /v0.129.0/hugo_0.129.0_linux-amd64.deb
x64_deb_url = (
    release_url + "/download/" + vversion + "/"
    + name + "_" + version + "_linux-amd64.deb"
)

check_download(name, version, x64_deb_url)
