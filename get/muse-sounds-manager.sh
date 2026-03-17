# AMD64
AMD64_URL="https://muse-cdn.com/Muse_Sounds_Manager_x64.deb"
Last_Modified=$(curl -sI $AMD64_URL | grep "last-modified")
# Last-Modified: Wed, 06 Nov 2024 02:08:50 GMT
VERSION=$(echo $Last_Modified | cut -d ' ' -f 3-6 | sed 's/ /-/g')
# 06-Nov-2024-02:08:50

./check_downloader.py muse-sounds-manager $VERSION $AMD64_URL amd64
