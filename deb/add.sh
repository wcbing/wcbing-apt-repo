echo "deb [trusted=yes] https://packages.wcbing.top/deb/$(dpkg --print-architecture) /" > \
    /etc/apt/sources.list.d/wcbing.list
apt update
