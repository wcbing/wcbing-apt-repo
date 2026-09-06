JSON=$(curl -s https://download.codebuddy.cn/workbuddy/saas/version.json)

AMD64_VERSION=$(echo "$JSON" | jq -r '."linux-x64-deb".stable.version')
AMD64_URL="https://download.codebuddy.cn/workbuddy/saas/linux-x64-deb/WorkBuddy-linux-x64-deb-$AMD64_VERSION.deb"
./check_downloader.py workbuddy "$AMD64_VERSION" "$AMD64_URL" amd64

ARM64_VERSION=$(echo "$JSON" | jq -r '."linux-arm64-deb".stable.version')
ARM64_URL="https://download.codebuddy.cn/workbuddy/saas/linux-arm64-deb/WorkBuddy-linux-arm64-deb-$ARM64_VERSION.deb"
./check_downloader.py workbuddy "$ARM64_VERSION" "$ARM64_URL" arm64
