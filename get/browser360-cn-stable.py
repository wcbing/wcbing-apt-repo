import requests
import json
from module.check import deb

version_json = json.loads(requests.get("https://active.browser.360.net/api/v1/web-version").text)
version = version_json["data"]["web_version"]

x64_deb_url = f"https://gedown.360safe.com/gc/browser360-cn-stable_{version}-1_amd64.deb"

deb("browser360-cn-stable", version, x64_deb_url)