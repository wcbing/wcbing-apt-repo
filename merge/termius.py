import requests

repo = "https://deb.termius.com/"

x64_deb_Packages_url = repo + "dists/squeeze/main/binary-amd64/Packages"
x64_deb_Packages = requests.get(x64_deb_Packages_url).text

x64_deb_content = x64_deb_Packages.replace("Filename: ", "Filename: " + repo)
# print(x64_deb_content)

with open("deb/Packages", "a+") as f:
    f.write(x64_deb_content)

f.close()

print("termius repo: done")
