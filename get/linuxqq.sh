JSON=$(curl -s https://im.qq.com/rainbow/linuxQQDownload | sed -nE 's/.*var params\s*=\s*(\{.*?\});.*/\1/p')

VERSION=$(echo $JSON | jq -r '.version + "_" + .updateDate')
X64_URL=$(echo $JSON | jq -r '.x64DownloadUrl.deb')

./check_downloader.py linuxqq $VERSION $X64_URL
