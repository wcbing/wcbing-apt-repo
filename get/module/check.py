import requests
import os
import sqlite3


def check_download(name, version, url, arch, file_type):
    conn = sqlite3.connect(file_type + ".db")
    cur = conn.cursor()

    res = cur.execute(
        "SELECT version, url FROM " + arch + " WHERE name = ?", (name,)
    ).fetchall()
    if len(res):
        db_version = res[0][0]
        db_url = res[0][1]
        print(name + ": " + db_version)
        if db_version != version:
            print("└  Update: " + db_version + " -> " + version)
            # download
            file_path = os.path.join(file_type, str(url.split("/")[-1]))
            with open(file_path, "wb") as fw:
                fw.write(requests.get(url).content)
            # wirte to db
            cur.execute(
                "UPDATE " + arch + " SET version = ?, url = ? WHERE name = ?",
                (version, url, name),
            )
            # remove old version
            old_file_path = os.path.join(file_type, str(db_url.split("/")[-1]))
            if os.path.exists(old_file_path):
                os.remove(old_file_path)
    else:
        print(name + "\n└  Add: " + version)
        # download
        file_path = os.path.join(file_type, str(url.split("/")[-1]))
        with open(file_path, "wb") as fw:
            fw.write(requests.get(url).content)
        # wirte to db
        cur.execute(
            "INSERT INTO " + arch + "(name, version, url) VALUES (?, ?, ?)",
            (name, version, url),
        )

    cur.close()
    conn.commit()
    conn.close()


def deb(name, version, url, arch="x86_64"):
    check_download(name, version, url, arch=arch, file_type="deb")
