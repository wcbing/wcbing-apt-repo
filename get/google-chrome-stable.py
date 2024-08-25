import requests
import re
from module.check import deb

deb_repo = "https://dl.google.com/linux/chrome/deb/"

x64_deb_list = requests.get(deb_repo + "dists/stable/main/binary-amd64/Packages").text

version = re.findall("-stable\nVersion: (.+)", x64_deb_list)[0]
x64_deb_url = deb_repo + re.findall("pool/.+-stable_.+.deb", x64_deb_list)[0]

deb("google-chrome-stable", version, x64_deb_url)
