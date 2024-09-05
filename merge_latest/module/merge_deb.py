def merge_latest_deb(name, repo, deb_latest, local_Packages_path="deb/Packages"):
    r"""Merge latest deb packages info from a repo to a Packages file

    :param name: repo name
    :param repo: repo url, end with "/"
    :param deb_latest: latest deb package info manually organized
    :param local_Packages_path: local Packages file path, default is "deb/Packages"
    :return: None
    """

    with open(local_Packages_path, "a+") as f:
        f.write(deb_latest.replace("Filename: ", "Filename: " + repo))
    f.close()
    print(name + " repo: done")
