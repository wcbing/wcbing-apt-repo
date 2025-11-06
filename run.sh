#!/bin/sh

# check for updates
./get-github-releases.py
find get -type f -name "*.sh" -exec sh {} \;

## merge the Packages file from local package
cat $(find packages -name "*.package") > deb/tmpPackages

## merge the Packages files from third-party repositories
./merge-apt-repo.py --local deb/tmpPackages

# generate the Release file
cd deb/dists/wcbing && \
echo 'Origin: wcbing APT Repo
Label: wcbing
Suite: wcbing
Codename: wcbing
Architectures: amd64 arm64
Components: main
Description: wcbing APT Repo || wcbing 的 APT 仓库' > Release && \
apt-ftparchive release . >> Release && \
gpg --yes --detach-sign -a -o Release.gpg Release && \
gpg --yes --clearsign -o InRelease Release
