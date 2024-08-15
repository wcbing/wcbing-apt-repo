import requests
from module.check import deb

name = "rustdesk"

release_url = "https://github.com/rustdesk/rustdesk/releases"

res = requests.head(release_url + "/latest", allow_redirects=False)
version = requests.Session().get_redirect_target(res).split("/")[-1]  # 1.1.1
# print(version)

# /1.2.7/rustdesk-1.2.7-x86_64.deb
x64_deb_url = (
    release_url + "/download/" + version + "/" + name + "-" + version + "-x86_64.deb"
)

deb(name, version, x64_deb_url)
