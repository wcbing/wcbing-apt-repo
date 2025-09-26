JSON=$(curl -s https://active.browser.360.net/api/v1/web-version)
VERSION=$(echo $JSON | jq -r ".data.web_version")

AMD64_URL="https://gedown.360safe.com/gc/browser360-cn-stable_"$VERSION"-1_amd64.deb"

./check_downloader.py browser360-cn-stable $VERSION $AMD64_URL amd64