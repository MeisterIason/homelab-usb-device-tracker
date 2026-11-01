import sqlite3
from pathlib import Path

def init_db(db_path: Path):
    conn = sqlite3.connect(db_path)
    conn.execute("""CREATE TABLE IF NOT EXISTS devices (
        vid TEXT, pid TEXT, serial TEXT PRIMARY KEY, first_seen TEXT, last_seen TEXT
    )""")
    conn.commit()
    return conn
