import requests
import re
from module.merge_deb import merge_latest_deb

deb_repo = "https://packages.mozilla.org/apt/"

x64_deb_Packages_path = "dists/mozilla/main/binary-amd64/Packages"
x64_deb_Packages = requests.get(deb_repo + x64_deb_Packages_path).text
x64_debs = re.split("(?=Package: )", x64_deb_Packages)[1:]

# firefox 的 Packages 按照版本升序排列，最后一个即为最新版本

firefox_x64_debs = []
firefox_beta_x64_debs = []
firefox_devedition_x64_debs = []
firefox_esr_x64_debs = []
firefox_nightly_x64_debs = []

for x64_deb in x64_debs:
    if "Package: firefox\n" in x64_deb:
        firefox_x64_debs.append(x64_deb)
    elif "Package: firefox-beta\n" in x64_deb:
        firefox_beta_x64_debs.append(x64_deb)
    elif "Package: firefox-devedition\n" in x64_deb:
        firefox_devedition_x64_debs.append(x64_deb)
    elif "Package: firefox-esr\n" in x64_deb:
        firefox_esr_x64_debs.append(x64_deb)
    elif "Package: firefox-nightly\n" in x64_deb:
        firefox_nightly_x64_debs.append(x64_deb)

x64_deb_latest = (
    firefox_x64_debs[-1]
    + firefox_beta_x64_debs[-1]
    + firefox_devedition_x64_debs[-1]
    + firefox_esr_x64_debs[-1]
    + firefox_nightly_x64_debs[-1]
    + "\n"
)

merge_latest_deb("firefox", deb_repo, x64_deb_latest)
