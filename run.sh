#!/bin/sh

# check for updates
find get -type f -name "*.sh" -exec sh {} \;

# generate the Packages file
## merge the Packages file from local package
cat $(find packages -name "*.package") >> deb/tmpPackages

## merge the Packages files from third-party repositories
./merge-apt-repo.py --local deb/tmpPackages

# generate the Release file
cd deb/dists/wcbing && \
apt-ftparchive release -c apt-ftparchive.conf . > Release && \
gpg --yes --detach-sign -a -o Release.gpg Release && \
gpg --yes --clearsign -o InRelease Release
