#!/bin/sh

gen_release() {
    apt-ftparchive release $1 >$1/Release
}

# check for updates
$HOME/go/bin/github-downloader -r -o deb
find get -type f -name "*.sh" -exec sh {} \;

cd deb
# generate the local Packages
apt-ftparchive packages . > tmpPackages
sed -i "s|\./http|http|g" tmpPackages

cd ..
sed -i "s|\./wtf|\.\./wtf|g" deb/tmpPackages
# merge the Packages files from third-party repositories
./merge-apt-repo.py --local deb/tmpPackages

# generate the Release file
gen_release deb/amd64
gen_release deb/amd64
