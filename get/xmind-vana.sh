AMD64_URL=$(curl -sI "https://xmind.cn/zen/download/linux_deb/" | grep location | cut -d ' ' -f 2 | tr -d '\r')

# https://dl3.xmind.cn/Xmind-for-Linux-amd64bit-24.04.10311-202405240010.deb
VERSION=$(echo $AMD64_URL | cut -d '-' -f 5)

./check_downloader.py xmind-vana $VERSION $AMD64_URL amd64
