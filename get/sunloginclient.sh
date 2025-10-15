JSON=$(curl -fs "https://client-webapi.oray.com/softwares/SUNLOGIN_X_LINUX?x64=1")

VERSION=$(printf "%s" "$JSON" | jq -r '.versionno')
AMD64_URL=$(printf "%s" "$JSON" | jq -r '.downloadurl')

./check_downloader.py sunloginclient $VERSION $AMD64_URL amd64