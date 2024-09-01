import requests
from module.check import deb

req = requests.get("https://www.dingtalk.com/win/d/qd=linux_amd64", allow_redirects=False)

x64_deb_url = req.headers['Location']
version = x64_deb_url.split("/")[-1].split("_")[1]

deb("com.alibabainc.dingtalk", version, x64_deb_url)
