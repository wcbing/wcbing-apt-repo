import requests
import re
from module.check import deb

res = requests.get("https://www.todesk.com/linux.html")

x64_url = re.findall("https://[0-9a-zA-Z_/.-]*.deb", res.text)[0]

# https://dl.todesk.com/linux/todesk-v4.7.2.0-amd64.deb
version = x64_url.split("-")[1]

deb("todesk", version, x64_url)
