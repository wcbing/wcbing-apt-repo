import requests
import re
from module.check import check_download

res = requests.get("https://y.qq.com/download/download.html")
res.encoding = "utf-8"

version = re.findall(
    r"Linux <span class=\"product_list__version\">最新版:(\d+\.\d+\.\d+)</span>",
    res.text,
)[0]
x64_deb_url = re.findall(r"https://dl\S+\.deb", res.text)[0]
# print(version, x64_deb_url)

check_download("qqmusic", version, x64_deb_url)
