#!/usr/bin/env python3

import os
import sqlite3

# create dir
if not os.path.exists("deb/amd64"):
    os.makedirs("deb/amd64")
if not os.path.exists("deb/arm64"):
    os.makedirs("deb/arm64")

# create table
conn = sqlite3.connect("data/deb.db")
conn.execute(
    """
        CREATE TABLE IF NOT EXISTS x86_64 (
            name TEXT UNIQUE,
            version TEXT,
            url TEXT
        );
    """
)
conn.execute(
    """
        CREATE TABLE IF NOT EXISTS arm64 (
            name TEXT UNIQUE,
            version TEXT,
            url TEXT
        );
    """
)

conn.commit()
conn.close()
