import requests

repo = "https://dl.google.com/linux/chrome/deb/"

x64_deb_Packages_url = repo + "dists/stable/main/binary-amd64/Packages"
x64_deb_Packages = requests.get(x64_deb_Packages_url).text

x64_deb_content = x64_deb_Packages.replace("Filename: ", "Filename: " + repo)
# print(x64_deb_content)

with open("deb/Packages", "a+") as f:
    f.write(x64_deb_content)

f.close()

print("google-chrome repo: done")
