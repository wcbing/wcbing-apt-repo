import requests
import re
from module.check import check_download

x64_deb_req = "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"

res = requests.head(x64_deb_req)
version = re.findall("_(.*)-", res.headers["Location"])[0]
x64_deb_url = res.headers["Location"]
# print(version, x64_deb_url)

check_download("code", version, x64_deb_url)
