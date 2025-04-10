X64_URL=$(curl -sw %{redirect_url} https://www.dingtalk.com/win/d/qd=linux_amd64)
VERSION=$(echo $X64_URL | sed 's#.*/##g' | cut -d '_' -f 2)
./check_downloader.py com.alibabainc.dingtalk $VERSION $X64_URL

ARM64_URL=$(curl -sw %{redirect_url} https://www.dingtalk.com/win/d/qd=linux_arm64)
VERSION=$(echo $ARM64_URL | sed 's#.*/##g' | cut -d '_' -f 2)
./check_downloader.py com.alibabainc.dingtalk $VERSION $ARM64_URL arm64
