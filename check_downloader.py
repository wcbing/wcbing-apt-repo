#!/usr/bin/env python3
import subprocess
import os
import sqlite3
import sys
import logging
import re
from threading import Lock

DEB_BASE_DIR = "deb"
PACKAGES_DIR = "packages"
DB_DIR = "data"
USER_AGENT = "Debian APT-HTTP/1.3 (3.0.3)"  # from Debian 13

version_lock = Lock()

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
    level=logging.INFO,
)


def download(url: str, file_path: str) -> bool:
    """Download file using curl with APT User-Agent."""
    curl_process = subprocess.run(
        ["curl", "-H", f"User-Agent: {USER_AGENT}", "-fsLo", file_path, url]
    )
    if curl_process.returncode or not os.path.exists(file_path):
        logging.error(f"Failed to download {url}")
        return False
    return True


def scan(name, arch, url, file_path) -> bool:
    scan_process = subprocess.run(
        ["apt-ftparchive", "packages", file_path], capture_output=True
    )
    package = scan_process.stdout.decode()
    package = re.sub(
        r"^(Filename: ).*", f"\\1{url}", package, flags=re.MULTILINE
    )  # 替换 Filename 开头的行

    package_file_path = os.path.join(PACKAGES_DIR, arch, f"{name}.package")

    try:
        with open(package_file_path, "w") as f:
            f.write(package)
            return True
    except IOError as e:
        logging.error(f"Failed to write package file for {name}: {e}")
        return False


def check_download(name: str, version: str, url: str, arch: str) -> None:
    """Check and handle package download/update."""
    logging.info("%s:%s = %s", name, arch, version)

    file_path = os.path.join(DEB_BASE_DIR, arch, f"{name}_{version}_{arch}.deb")
    local_version = None
    db_path = os.path.join(DB_DIR, f"{DEB_BASE_DIR}.db")
    # get local version
    with version_lock, sqlite3.connect(db_path) as conn:
        res = conn.execute(
            f"SELECT version FROM '{arch}' WHERE name = ?", (name,)
        ).fetchone()
    if res:
        local_version = res[0]
        if local_version == version:
            return

    # download and scan
    logging.info(f"Downloading {name}:{arch} ({version})")
    os.makedirs(os.path.join(DEB_BASE_DIR, arch), exist_ok=True)
    if not download(url, file_path):
        return
    logging.info(f"Downloaded {name}:{arch} ({version})")
    os.makedirs(os.path.join(PACKAGES_DIR, arch), exist_ok=True)
    if not scan(name, arch, url, file_path):
        return

    if res:
        print(f"Update: {name}:{arch} ({local_version} -> {version})")
        # update database
        with version_lock, sqlite3.connect(db_path) as conn:
            conn.execute(
                f"UPDATE '{arch}' SET version = ?, url = ? WHERE name = ?",
                (version, url, name),
            )
            conn.commit()
        # remove old version
        old_file_path = os.path.join(DEB_BASE_DIR, arch, f"{name}_{local_version}_{arch}.deb")
        if os.path.exists(old_file_path):
            os.remove(old_file_path)
    else:
        print(f"AddNew: {name}:{arch} ({version})")
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
