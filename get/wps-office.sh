# decrypt() {
#     url=$1
#     pathname="/$(echo $url | cut -d '/' -f 4-)"
#     secrity_key="7f8faaaa468174dc1c9cd62e5f218a5b"
#     timestamp10=$(date '+%s')
#     md5hash=$(echo -n "${secrity_key}${pathname}${timestamp10}" | md5sum | cut -d " " -f 1 )
#     url="$url?t=${timestamp10}&k=${md5hash}"
#     echo $url
# }

# WPS 官网 JS 代码大致逻辑如下：
# function downLoad(url) {
#   var urlObj=new URL(url);
#   var uri=urlObj.pathname;
#   var secrityKey="7f8faaaa468174dc1c9cd62e5f218a5b";
#   var timestamp10=Math.floor(new Date().getTime() / 1000);
#   var md5hash=CryptoJS.MD5(secrityKey + uri + timestamp10);
#   url += '?t=' + timestamp10 + '&k=' + md5hash
#   console.log(url);
# }

WEB_CONTENT=$(curl -fs https://linux.wps.cn/)
VERSION=$(echo $WEB_CONTENT | grep -o "<p class=\"banner_txt\">[0-9.]*</p>" | sed 's/<p class=\"banner_txt\">\(.*\)<\/p>/\1/')
AMD64_ORI_URL=$(echo $WEB_CONTENT | grep -o "https://[0-9a-zA-Z_\/\.\-]*amd64\.deb" | head -n 1)

# AMD64_URL=$(decrypt $AMD64_ORI_URL)
# 使用 CloudFlare Workers 动态生成重定向链接，其基本逻辑如上方 JS 代码所示。
# 这样 Packages 中固定链接也可重定向至官网，不给官方白嫖流量的机会。
AMD64_URL="https://wps302.wcbing.workers.dev/$AMD64_ORI_URL"

./check_downloader.py wps-office $VERSION $AMD64_URL amd64