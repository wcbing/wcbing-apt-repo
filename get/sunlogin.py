import requests
from module.check import deb

req = requests.get("https://client-webapi.oray.com/softwares/SUNLOGIN_X_LINUX?x64=1")
version = req.json()["versionno"]
x64_url = req.json()["downloadurl"]

deb("sunloginclient", version, x64_url)