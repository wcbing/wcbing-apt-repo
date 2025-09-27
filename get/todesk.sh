AMD64_URL=$(curl -s https://www.todesk.com/linux.html | grep -o "https://[0-9a-zA-Z_\/\.\-]*.deb" | head -n 1)
# AMD64_URL=https:/ /dl.todesk.com/linux/todesk-v4.7.2.0-amd64.deb

VERSION=$(echo $AMD64_URL | cut -d '-' -f 2)

./check_downloader.py todesk $VERSION $AMD64_URL amd64