X64_JSON=$(curl -s "https://www.feishu.cn/api/package_info?platform=10")
# arm64 https://www.feishu.cn/api/package_info?platform=12

# "version_number": "Linux-x64-deb@V7.22.9"
VERSION=$(echo $X64_JSON | jq -r ".data.version_number" | cut -d 'V' -f 2)
X64_URL=$(echo $X64_JSON | jq -r ".data.download_link")

./check_downloader.py bytedance-feishu-stable $VERSION $X64_URL
