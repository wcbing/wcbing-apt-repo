#!/bin/sh

date
# check for updates
$HOME/go/bin/github-downloader -r -o deb
find get -maxdepth 1 -type f -name "*.sh" -exec sh {} \;
cd deb
# generate the local Packages
apt-ftparchive packages . > tmpPackages
cd ..

sed -i "s/\.\/http/\.\.\/http/g" deb/tmpPackages
# merge the Packages files of third-party repositories
./merge-apt-repo.py --local deb/tmpPackages

# generate the Release file
cd deb/amd64
apt-ftparchive release . > Release
cd ../arm64
apt-ftparchive release . > Release

echo done