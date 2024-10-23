import requests
from module.check import deb

x64_deb_req = requests.head("https://dida365.com/static/getApp/download?type=linux_deb_x64", headers={"User-Agent": "curl/8.10.1"})
# arm64_deb_req = requests.head("https://dida365.com/static/getApp/download?type=linux_deb_arm64", headers={"User-Agent": "curl/8.10.1"})

x64_deb_url = x64_deb_req.headers["location"]
# https://cdn.dida365.cn/download/linux/linux_deb_x64/dida-6.0.0-amd64.deb
version = x64_deb_url.split("-")[-2]

deb("dida", version, x64_deb_url)
