# 正式版参考 https://github.com/flathub/com.qq.QQ/blob/master/com.qq.QQ.yaml
# JSON=$(curl -s https://cdn-go.cn/qq-web/im.qq.com_new/latest/rainbow/pcConfig.json | jq '.Linux')
# VERSION=$(echo $JSON | jq -r '.version + "_" + .updateDate')

# 测试版参考 https://bbs.deepin.org/post/279737?offset=1&limit=20&postId=1658175
WEB_CONTENT=$(curl -fs 'https://docs.qq.com/dop-api/opendoc?u&id=DVXNoRlpKaWhEY015&normal=1&noEscape=1&callback=clientVarsCallback' -H 'referer: https://docs.qq.com/doc/DVXNoRlpKaWhEY015')

# AMD64
AMD64_URL=$(echo $WEB_CONTENT | grep -o "https:[0-9a-zA-Z/._-]*_amd64\.deb" | head -n 1)
VERSION=$(echo $AMD64_URL | sed -E 's/.*linuxqq_(.*)_amd64.*/\1/')
./check_downloader.py linuxqq $VERSION $AMD64_URL amd64

# ARM64
ARM64_URL=$(echo $WEB_CONTENT | grep -o "https:[0-9a-zA-Z/._-]*_arm64\.deb" | head -n 1)
VERSION=$(echo $ARM64_URL | sed -E 's/.*linuxqq_(.*)_arm64.*/\1/')
./check_downloader.py linuxqq $VERSION $ARM64_URL arm64