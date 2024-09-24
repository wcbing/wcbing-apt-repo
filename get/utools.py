import requests
import re
from module.check import deb

res = requests.get("https://u.tools/download/")
res.encoding = "utf-8"

x64_deb_url = re.findall(r"https:\/\/[^ ]+\.deb", res.text)[0]
version = re.findall(".*utools_(.+)_amd64.deb", x64_deb_url)[0]

deb("utools", version, x64_deb_url)
