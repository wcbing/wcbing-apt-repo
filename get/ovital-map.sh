WEB_CONTENT=$(curl -s https://www.ovital.com/download/)

VERSION=$(echo "$WEB_CONTENT" | grep -m 1 -oP "奥维互动地图Linux客户端 V\K[0-9\.]*")

DEB_LIST=$(echo "$WEB_CONTENT" | grep -o "https://[0-9a-zA-Z_\/\.\-]*.deb")

# AMD64
AMD64_URL=$(echo "$DEB_LIST" | grep "x86_64")
./check_downloader.py ovital-map "$VERSION" "$AMD64_URL" amd64

# ARM64
ARM64_URL=$(echo "$DEB_LIST" | grep "aarch64")
./check_downloader.py ovital-map "$VERSION" "$ARM64_URL" arm64
