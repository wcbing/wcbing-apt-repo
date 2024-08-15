import requests
import json
from module.check import deb

version_url = "https://versionhistory.googleapis.com/v1/chrome/platforms/linux/channels/stable/versions"
res = requests.get(version_url)
version = json.loads(res.text)["versions"][0]["version"]
# print(version)

x64_deb_url = "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"

deb("google-chrome-stable", version, x64_deb_url)
