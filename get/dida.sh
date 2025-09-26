AMD64_URL=$(curl -sI "https://dida365.com/static/getApp/download?type=linux_deb_x64" | grep location | cut -d ' ' -f 2 | tr -d '\r')
# https://cdn.dida365.cn/download/linux/linux_deb_x64/dida-6.0.0-amd64.deb
VERSION=$(echo $AMD64_URL | cut -d "-" -f 2)
./check_downloader.py dida $VERSION $AMD64_URL amd64

# ARM64
ARM64_URL=$(curl -sI "https://dida365.com/static/getApp/download?type=linux_deb_arm64" | grep location | cut -d ' ' -f 2 | tr -d '\r')
VERSION=$(echo $ARM64_URL | cut -d "-" -f 2)
./check_downloader.py dida $VERSION $ARM64_URL arm64
