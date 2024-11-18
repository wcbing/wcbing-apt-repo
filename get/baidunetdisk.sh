JSON=$(curl -s "https://pan.baidu.com/disk/cmsdata?do=client")

VERSION=$(echo $JSON | jq -r ".linux.version" | cut -d "V" -f 2)
X64_URL=$(echo $JSON | jq -r ".linux.url_1")

./check_downloader.py baidunetdisk $VERSION $X64_URL