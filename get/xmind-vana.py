import requests
from module.check import deb

x64_deb_req = requests.head("https://xmind.cn/zen/download/linux_deb/")

x64_deb_url = x64_deb_req.headers["Location"]
# https://dl3.xmind.cn/Xmind-for-Linux-amd64bit-24.04.10311-202405240010.deb
version = x64_deb_url.split("-")[-2]

deb("xmind-vana", version, x64_deb_url)
