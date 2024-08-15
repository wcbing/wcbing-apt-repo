import requests
import re
from module.check import deb

x64_deb_url = "https://go.microsoft.com/fwlink?linkid=2149051"

res = requests.head(x64_deb_url)
version = re.findall("_(.*)_", res.headers["Location"])[0]
x64_deb_url = res.headers["Location"]
# print(version, x64_deb_url)

deb("microsoft-edge-stable", version, x64_deb_url)
