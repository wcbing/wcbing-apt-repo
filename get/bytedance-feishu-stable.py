import requests
import json
from module.check import deb

x64_deb_res = requests.get("https://www.feishu.cn/api/package_info?platform=10")
x64_deb_json = json.loads(x64_deb_res.text)

# "version_number": "Linux-x64-deb@V7.22.9"
version = x64_deb_json["data"]["version_number"].split("@V")[1]
x64_deb_url = x64_deb_json["data"]["download_link"]

deb("bytedance-feishu-stable", version, x64_deb_url)
