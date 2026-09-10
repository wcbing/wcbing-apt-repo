WEB_CONTENT=$(curl -s https://www.eudic.net/v4/en/app/download)

AMD64_URL=$(echo $WEB_CONTENT | grep -o 'https://[^"]*\.deb[^"]*')
# https://www.eudic.net/download/eudic.deb?v=2025-08-25
VERSION=$(echo $AMD64_URL | cut -d '=' -f 2)

./check_downloader.py eudic "$VERSION" "$AMD64_URL" amd64
