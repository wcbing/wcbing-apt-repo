WEB_CONTENT="https://www.mossgrabers.de/Software/ConvertWithMoss/ConvertWithMoss-Installers-ubuntu-latest/"

VERSION=$(curl -s "$WEB_CONTENT" | grep -oP 'convertwithmoss_\K[0-9.]+(?=_amd64.deb)' | sort -V | tail -n1)

AMD64_URL="${WEB_CONTENT}convertwithmoss_${VERSION}_amd64.deb"

./check_downloader.py convertwithmoss "$VERSION" "$AMD64_URL" amd64
