#!/bin/sh

# check for updates
date
find get -maxdepth 1 -type f -name "*.py" -exec python3 {} \;

# generate the files
cd deb
apt-ftparchive packages . > Packages
apt-ftparchive release . > Release
gpg --yes --armor --detach-sign --sign -o Release.gpg Release
gpg --yes --clearsign -o InRelease Release

echo done