WEB_CONTENT=$(curl -s "https://www.u-tools.cn/download/")

AMD64_URL=$(echo $WEB_CONTENT | grep -o "https://[^ ]*amd64\.deb")

# https://open.u-tools.cn/download/utools_5.2.1_amd64.deb
VERSION=$(echo $AMD64_URL | cut -d '_' -f 2)

./check_downloader.py utools $VERSION $AMD64_URL amd64
