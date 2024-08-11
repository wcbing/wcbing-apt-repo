import requests
import re
import json
from module.check import check_download

res = requests.get("https://im.qq.com/rainbow/linuxQQDownload")
res.encoding = "utf-8"

download_list_json = re.search(
    r"var params\s*=\s*(\{.*?\});", res.text, re.DOTALL
).group(1)
download_list = json.loads(download_list_json)

version = download_list["version"]
x64_deb_url = download_list["x64DownloadUrl"]["deb"]
# print(version, x64_deb_url)

check_download("linuxqq", version, x64_deb_url)
