import requests
import re
import time
import hashlib
from module.check import deb

res = requests.get("https://linux.wps.cn/")
res.encoding = "utf-8"

version = re.findall(r"<p class=\"banner_txt\">(.*)</p>", res.text)[0]

"""js
function downLoad(url) {
  var urlObj = new URL(url);
  var uri = urlObj.pathname;
  var secrityKey = "7f8faaaa468174dc1c9cd62e5f218a5b";
  var timestamp10 = Math.floor(new Date().getTime() / 1000);
  var md5hash = CryptoJS.MD5(secrityKey + uri + timestamp10);
  url += '?t=' + timestamp10 + '&k=' + md5hash
  console.log(url);
}
"""

secrityKey = "7f8faaaa468174dc1c9cd62e5f218a5b"
timestamp10 = str(int(time.time()))

x64_deb_url = re.findall(r"https://.*/wps/download/.*_amd64.deb", res.text)[0]
x64_deb_pathname = "/" + "/".join(x64_deb_url.split("/")[3:])
x64_deb_md5hash = hashlib.md5(str.encode(secrityKey + x64_deb_pathname + timestamp10))
x64_deb_url += '?t=' + timestamp10 + '&k=' + x64_deb_md5hash.hexdigest()

# print(version, x64_deb_url)

deb("wps-office", version, x64_deb_url)
