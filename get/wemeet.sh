# https://meeting.tencent.com/web-service/query-download-info?q=[\
# {"package-type":"app","channel":"0300000000","platform":"linux","arch":"x86_64","decorators":["deb"]},\
# {"package-type":"app","channel":"0300000000","platform":"linux","arch":"arm64","decorators":["deb"]},\
# {"package-type":"app","channel":"0300000000","platform":"linux","arch":"loongarch64","decorators":["deb"]}\
# ]&nonce=D38mxpWk6TMTA44a

download_list_url="https://meeting.tencent.com/web-service/query-download-info?q=%5B\
%7B%22package-type%22%3A%22app%22%2C%22channel%22%3A%220300000000%22%2C%22platform%22%3A%22linux%22%2C%22arch%22%3A%22x86_64%22%2C%22decorators%22%3A%5B%22deb%22%5D%7D%2C\
%7B%22package-type%22%3A%22app%22%2C%22channel%22%3A%220300000000%22%2C%22platform%22%3A%22linux%22%2C%22arch%22%3A%22arm64%22%2C%22decorators%22%3A%5B%22deb%22%5D%7D%2C\
%7B%22package-type%22%3A%22app%22%2C%22channel%22%3A%220300000000%22%2C%22platform%22%3A%22linux%22%2C%22arch%22%3A%22loongarch64%22%2C%22decorators%22%3A%5B%22deb%22%5D%7D\
%5D&nonce=D38mxpWk6TMTA44a"

JSON=$(curl -s $download_list_url)

VERSION=$(echo $JSON | jq -r '."info-list"[0].version')
X64_URL=$(echo $JSON | jq -r '."info-list"[0].url')
./check_downloader.py wemeet $VERSION $X64_URL

# ARM64
VERSION=$(echo $JSON | jq -r '."info-list"[1].version')
ARM64_URL=$(echo $JSON | jq -r '."info-list"[1].url')
./check_downloader.py wemeet $VERSION $ARM64_URL arm64
