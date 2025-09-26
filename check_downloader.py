#!/usr/bin/env python3
import subprocess
import os
import sqlite3
import sys
import logging
from threading import Lock

BASE_DIR = "deb"
DB_DIR = "data"
USER_AGENT = "Debian APT-HTTP/1.3 (2.6.1)"  # from Debian 12

version_lock = Lock()

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
    level=logging.INFO,
)


def download(url: str) -> None:
    """Download file using curl with APT User-Agent."""
    file_path = os.path.join(BASE_DIR, url.split("?")[0])
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    subprocess.run(["curl", "-H", f"User-Agent: {USER_AGENT}", "-fsLo", file_path, url])


def check_download(name: str, version: str, url: str, arch: str) -> None:
    """Check and handle package download/update."""
    logging.info("%s:%s = %s", name, arch, version)

    db_path = os.path.join("data", f"{BASE_DIR}.db")
    # get local version
    with version_lock, sqlite3.connect(db_path) as conn:
        res = conn.execute(
            f"SELECT version, url FROM '{arch}' WHERE name = ?", (name,)
        ).fetchone()
    if res:
        local_version, local_url = res
        if local_version != version:
            print(f"Update: {name}:{arch} ({local_version} -> {version})")
            download(url)
            # update database
            with version_lock, sqlite3.connect(db_path) as conn:
                conn.execute(
                    f"UPDATE '{arch}' SET version = ?, url = ? WHERE name = ?",
                    (version, url, name),
                )
                conn.commit()
            # remove old version
            if local_url != url:  # 防止固定下载链接
                old_file_path = os.path.join(BASE_DIR, local_url.split("?")[0])
                if os.path.exists(old_file_path):
                    os.remove(old_file_path)
    else:
        print(f"AddNew: {name}:{arch} ({version})")
        download(url)
        # update database
        with version_lock, sqlite3.connect(db_path) as conn:
            conn.execute(
                f"INSERT INTO '{arch}'(name, version, url) VALUES (?, ?, ?)",
                (name, version, url),
            )
            conn.commit()


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 5:
        check_download(*args[1:])
    elif len(args) > 1:
        logging.error(f"Unknown Args: {args[1:]}")
    else:
        print(f"Usage: {args[0]} <package_name> <version> <url> <arch>")
        print("options:")
        print("    arch: amd64, arm64, all.")
