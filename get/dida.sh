X64_URL=$(curl -sI "https://dida365.com/static/getApp/download?type=linux_deb_x64" | grep location | cut -d ' ' -f 2)
# arm64 https://dida365.com/static/getApp/download?type=linux_deb_arm64

# https://cdn.dida365.cn/download/linux/linux_deb_x64/dida-6.0.0-amd64.deb
VERSION=$(echo $X64_URL | cut -d "-" -f 2)

./check_downloader.py dida $VERSION $X64_URL
