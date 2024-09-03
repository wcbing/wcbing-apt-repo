import requests
from module.check import deb

release_url = "https://github.com/rustdesk/rustdesk/releases"

latest_req = requests.head(release_url + "/latest")
version = latest_req.headers["Location"].split("/")[-1]  # 1.1.1
# print(version)

# /1.2.7/rustdesk-1.2.7-x86_64.deb
x64_deb_url = (
    release_url + "/download/" + version + "/rustdesk-" + version + "-x86_64.deb"
)

deb("rustdesk", version, x64_deb_url)
