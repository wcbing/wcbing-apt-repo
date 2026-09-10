AMD64_URL=$(curl -s https://www.eudic.net/v4/en/app/download | grep -o 'https://[^"]*\.deb[^"]*')
tmp=$(mktemp)
curl -sL -o "$tmp" "$AMD64_URL"
REAL_VERSION=$(dpkg-deb -f "$tmp" Version)
rm -f "$tmp"
echo "$REAL_VERSION"   # 应该是 13.5.2(20260910)

./check_downloader.py eudic "$REAL_VERSION" "$AMD64_URL" amd64
