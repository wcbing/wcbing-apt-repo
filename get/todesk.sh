AMD64_URL=$(curl -s https://www.todesk.com/linux.html \
  | sed 's/\\u002F/\//g' \
  | grep -oE 'https://dl\.todesk\.com/linux/todesk-v[0-9.]+-amd64\.deb' \
  | head -n 1)
# AMD64_URL=https:/ /dl.todesk.com/linux/todesk-v4.7.2.0-amd64.deb

VERSION=$(echo $AMD64_URL | cut -d '-' -f 2)

./check_downloader.py todesk $VERSION $AMD64_URL amd64
