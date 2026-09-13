AMD64_API_JSON=$(curl -s https://copilot.tencent.com/v2/update?platform=workbuddy-linux-x64-deb)
AMD64_VERSION=$(echo "$AMD64_API_JSON" | jq -r '.version')
AMD64_URL=$(echo "$AMD64_API_JSON" | jq -r '.url')
./check_downloader.py workbuddy "$AMD64_VERSION" "$AMD64_URL" amd64

ARM64_API_JSON=$(curl -s https://copilot.tencent.com/v2/update?platform=workbuddy-linux-arm64-deb)
ARM64_VERSION=$(echo "$ARM64_API_JSON" | jq -r '.version')
ARM64_URL=$(echo "$ARM64_API_JSON" | jq -r '.url')
./check_downloader.py workbuddy "$ARM64_VERSION" "$ARM64_URL" arm64
