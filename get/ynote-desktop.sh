# AMD64
AMD64_URL="https://artifact.lx.netease.com/download/ynote-electron/%E6%9C%89%E9%81%93%E4%BA%91%E7%AC%94%E8%AE%B0-web.deb"
Last_Modified=$(curl -sLI $AMD64_URL | grep "last-modified")
# last-modified: Thu, 12 Mar 2026 05:57:49 GMT
VERSION=$(echo $Last_Modified | cut -d ' ' -f 3-6 | sed 's/ /-/g')
# 12-Mar-2026-05:57:49

./check_downloader.py ynote-desktop $VERSION $AMD64_URL amd64
