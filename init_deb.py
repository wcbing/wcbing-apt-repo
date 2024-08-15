#!/bin/python3

import os
import sqlite3

# create dir
os.mkdir("deb")

# create table
conn = sqlite3.connect("deb.db")
conn.execute(
    """
        CREATE TABLE IF NOT EXISTS x86_64 (
            name TEXT UNIQUE,
            version TEXT,
            url TEXT
        );
    """
)
# conn.execute(
#     """
#         CREATE TABLE IF NOT EXISTS arm64 (
#             name TEXT UNIQUE,
#             version TEXT,
#             url TEXT
#         );
#     """
# )

conn.commit()
conn.close()
