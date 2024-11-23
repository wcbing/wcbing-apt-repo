#!/bin/sh

date
# import go tools
export PATH="$PATH:$HOME/go/bin/"
# merge the Packages files of third-party repositories
rm deb/Packages
merge-apt-repo

# check for updates
github-downloader -r -o deb
find get -maxdepth 1 -type f -name "*.sh" -exec sh {} \;

# generate the files
cd deb
apt-ftparchive packages . >> Packages

# list brief information about packages
cat Packages | grep "Package\|Version\|Architecture\|^\$" > version.txt
# generate the Release file
apt-ftparchive release . > Release
gpg --yes --armor --detach-sign --sign -o Release.gpg Release
gpg --yes --clearsign -o InRelease Release

echo done