# 正式版参考 https://github.com/flathub/com.qq.QQ/blob/master/com.qq.QQ.yaml
JSON=$(curl -s https://cdn-go.cn/qq-web/im.qq.com_new/latest/rainbow/linuxConfig.js | sed -nE 's/.*var params\s*=\s*(\{.*?\});.*/\1/p')
VERSION=$(echo $JSON | jq -r '.version + "_" + .updateDate')

# 测试版参考 https://bbs.deepin.org/post/279737?offset=1&limit=20&postId=1658175

# AMD64
AMD64_URL=$(echo $JSON | jq -r '.x64DownloadUrl.deb')
./check_downloader.py linuxqq $VERSION $AMD64_URL amd64

# ARM64
ARM64_URL=$(echo $JSON | jq -r '.armDownloadUrl.deb')
./check_downloader.py linuxqq $VERSION $ARM64_URL arm64