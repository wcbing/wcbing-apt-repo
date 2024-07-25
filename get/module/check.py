import requests
import os
import sqlite3


def check_download(name, version, url, arch="x86_64"):
    conn = sqlite3.connect("deb.db")
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
            # remove old version
            old_file_path = os.path.join("deb", str(db_url.split("/")[-1]))
            if os.path.exists(old_file_path):
                os.remove(old_file_path)
            # download
            file_path = os.path.join("deb", str(url.split("/")[-1]))
            with open(file_path, "wb") as fw:
                fw.write(requests.get(url).content)
            # wirte to db
            cur.execute(
                "UPDATE " + arch + " SET version = ?, url = ? WHERE name = ?",
                (version, url, name),
            )
    else:
        print(name + "\n└  Add: " + version)
        # download
        file_path = os.path.join("deb", str(url.split("/")[-1]))
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
