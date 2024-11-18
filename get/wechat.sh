WEB_CONTENT=$(curl -s "https://linux.weixin.qq.com/")
X64_URL=$(echo $WEB_CONTENT | grep -o 'https:[0-9a-zA-Z/\._]*x86_64\.deb')

Last_Modified=$(curl -sI $X64_URL | grep "Last-Modified")
# Last-Modified: Wed, 06 Nov 2024 02:08:50 GMT
VERSION=$(echo $Last_Modified | cut -d ' ' -f 3-6 | sed 's/ /-/g')
# 06-Nov-2024-02:08:50

./check_downloader.py wechat $VERSION $X64_URL
