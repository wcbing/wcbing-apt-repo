# 参考 https://github.com/SpecterShell/Dumplings/blob/main/Tasks/Tencent.TencentDocs/Script.ps1

VERSION=$(curl -fs https://docs.qq.com/api/packageupgrade/update_manual | sed 's/.*"version\\\": \\\"\([0-9.]*\).*/\1/')
BASE_URL="https://desktop.docs.qq.com/update/release/$VERSION/"

AMD64_URL="$BASE_URL"$(curl -fs "$BASE_URL"latest-linux.yml | grep '^path' | cut -d ' ' -f 2)
./check_downloader.py tdappdesktop $VERSION $AMD64_URL amd64

ARM64_URL="$BASE_URL"$(curl -fs "$BASE_URL"latest-linux-arm64.yml | grep '^path' | cut -d ' ' -f 2)
./check_downloader.py tdappdesktop $VERSION $ARM64_URL arm64