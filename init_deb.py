#!/usr/bin/env python3

import sqlite3

# create table
conn = sqlite3.connect("data/deb.db")
for arch in ["amd64", "arm64", "all"]:
    conn.execute(
        f"""
            CREATE TABLE IF NOT EXISTS '{arch}' (
                name TEXT UNIQUE,
                version TEXT,
                url TEXT
            );
        """
    )

conn.commit()
conn.close()
