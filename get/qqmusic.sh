WEB_CONTENT=$(curl -s "https://y.qq.com/download/download.html")

VERSION=$(echo $WEB_CONTENT | grep -o "Linux <span class=\"product_list__version\">最新版:[0-9\.]*" | cut -d ':' -f 2)
AMD64_URL=$(echo $WEB_CONTENT | grep -o "https://[0-9a-z/\._]*amd64\.deb" | head -n 1)

./check_downloader.py qqmusic $VERSION $AMD64_URL amd64
