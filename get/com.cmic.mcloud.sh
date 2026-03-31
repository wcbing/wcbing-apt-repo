# 获取内容并筛选出银河麒麟相关信息
WEB_CONTENT=$(curl -s -X POST 'https://yun.139.com/platformInfo/advertapi/adv-filter/adv-filter/AdInfoFilter/getAdInfos' \
  -H 'Content-Type: application/json;charset=utf-8' \
  --data-raw '{"adpostid":2016,"client":"web","channel":"10000034","version":"0.0.0"}' \
  | jq -r '.body[2]')

AMD64_URL=$(echo "$WEB_CONTENT" | grep -o "https://[^']*\.deb")
# https://yun.mcloud.139.com/mCloudPc/kylinV110/com.cmic.mcloud_1.1.0_amd64.deb

VERSION=$(echo "$AMD64_URL" | cut -d '_' -f 2)

./check_downloader.py com.cmic.mcloud "$VERSION" "$AMD64_URL" amd64
