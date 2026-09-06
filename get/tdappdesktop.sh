# 参考 https://github.com/SpecterShell/Dumplings/blob/main/Tasks/Tencent.TencentDocs/Script.ps1

VERSION=$(curl -fs https://docs.qq.com/api/packageupgrade/update_manual | jq -r '.result.update_info' | jq -r '.version')

AMD64_URL="https://docs.qq.com/api/package/get?channel_id=30001&version_id=latest&package_name=TencentDocs-x64.deb"
./check_downloader.py tdappdesktop $VERSION $AMD64_URL amd64

ARM64_URL="https://docs.qq.com/api/package/get?channel_id=30001&version_id=latest&package_name=TencentDocs-arm64.deb"
./check_downloader.py tdappdesktop $VERSION $ARM64_URL arm64