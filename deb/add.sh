curl -fsSLo /etc/apt/keyrings/wcbing.gpg https://packages.wcbing.top/wcbing.gpg
echo "deb [signed-by=/etc/apt/keyrings/wcbing.gpg] https://packages.wcbing.top/deb /" > \
    /etc/apt/sources.list.d/wcbing.list
apt update
