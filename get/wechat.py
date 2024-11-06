import requests
import re
from module.check import deb

html = requests.get("https://linux.weixin.qq.com/").text
x64_deb_url = re.findall(r'href="(https:.*x86_64\.deb)"', html)[0]

last_modified = requests.head(x64_deb_url).headers["Last-Modified"]
# Wed, 06 Nov 2024 02:08:50 GMT
version = "-".join(last_modified.split(" ")[1:5])
# 06-Nov-2024-02:08:50

deb("wechat", version, x64_deb_url)
