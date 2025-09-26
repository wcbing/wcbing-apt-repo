WEB_CONTENT=$(curl -s "https://linux.weixin.qq.com/")

# AMD64
AMD64_URL=$(echo $WEB_CONTENT | grep -o 'https:[0-9a-zA-Z/\._]*x86_64\.deb')
Last_Modified=$(curl -sI $AMD64_URL | grep "Last-Modified")
# Last-Modified: Wed, 06 Nov 2024 02:08:50 GMT
VERSION=$(echo $Last_Modified | cut -d ' ' -f 3-6 | sed 's/ /-/g')
# 06-Nov-2024-02:08:50

./check_downloader.py wechat $VERSION $AMD64_URL amd64

# ARM64
ARM64_URL=$(echo $WEB_CONTENT | grep -o 'https:[0-9a-zA-Z/\._]*arm64\.deb')
Last_Modified=$(curl -sI $ARM64_URL | grep "Last-Modified")
VERSION=$(echo $Last_Modified | cut -d ' ' -f 3-6 | sed 's/ /-/g')

./check_downloader.py wechat $VERSION $ARM64_URL arm64