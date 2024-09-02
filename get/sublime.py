import requests
import re
from module.check import deb

req = requests.get("https://www.sublimetext.com/download_thanks?target=x64-deb")

x64_deb_url = re.findall('url = "(.*amd64.deb)"', req.text)[0]
# https://download.sublimetext.com/sublime-text_build-4180_amd64.deb
version = x64_deb_url.split("-")[-1].split("_")[0]

deb("sublime-text", version, x64_deb_url)
