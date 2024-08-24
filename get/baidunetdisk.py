import requests
import json
from module.check import deb

res = requests.get("https://pan.baidu.com/disk/cmsdata?do=client")
res.encoding = "utf-8"

download_list = json.loads(res.text)

version = download_list["linux"]["version"].split("V")[1]
x64_deb_url = download_list["linux"]["url_1"]
# print(version, x64_deb_url)

deb("baidunetdisk", version, x64_deb_url)
