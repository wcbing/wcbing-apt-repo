X64_URL=$(curl -sw %{redirect_url} https://www.dingtalk.com/win/d/qd=linux_amd64)
VERSION=$(echo $X64_URL | cut -d '/' -f 8| cut -d '_' -f 2)

./check_downloader.py com.alibabainc.dingtalk $VERSION $X64_URL
