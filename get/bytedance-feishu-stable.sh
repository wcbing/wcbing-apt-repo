VERSIONS_JSON=$(curl -fs "https://www.feishu.cn/api/downloads")

# AMD64
# "version_number": "Linux-x64-deb@V7.22.9"
AMD64_VERSION=$(echo $VERSIONS_JSON | jq -r ".versions.Linux_deb_x64.version_number" | cut -d 'V' -f 2)
AMD64_URL=$(echo $VERSIONS_JSON | jq -r ".versions.Linux_deb_x64.download_link")
./check_downloader.py bytedance-feishu-stable $AMD64_VERSION $AMD64_URL

# ARM64
ARM64_VERSION=$(echo $VERSIONS_JSON | jq -r ".versions.Linux_deb_arm.version_number" | cut -d 'V' -f 2)
ARM64_URL=$(echo $VERSIONS_JSON | jq -r ".versions.Linux_deb_arm.download_link")
./check_downloader.py bytedance-feishu-stable $ARM64_VERSION $ARM64_URL arm64
