JSON=$(curl -fs "https://client-webapi.oray.com/softwares/SUNLOGIN_X_LINUX?x64=1")

VERSION=$(echo "$JSON" | jq -r '.versionno')
X64_URL=$(echo $JSON | jq -r '.downloadurl')

./check_downloader.py sunloginclient $VERSION $X64_URL