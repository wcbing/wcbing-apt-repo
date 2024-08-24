import requests
import os
import sqlite3


def download(url, file_type):
    file_dir = os.path.join(file_type, "/".join(url.split("/")[:-1]))
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    file_path = os.path.join(file_type, url)
    with requests.get(url, stream=True) as res:
        with open(file_path, "wb") as fw:
            for chunk in res.iter_content(chunk_size=8192):
                if chunk:
                    fw.write(chunk)


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
            download(url, file_type)
            # wirte to db
            cur.execute(
                "UPDATE " + arch + " SET version = ?, url = ? WHERE name = ?",
                (version, url, name),
            )
            # remove old version
            old_file_path = os.path.join(file_type, db_url)
            if os.path.exists(old_file_path):
                os.remove(old_file_path)
    else:
        print(name + "\n└  Add: " + version)
        download(url, file_type)
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
