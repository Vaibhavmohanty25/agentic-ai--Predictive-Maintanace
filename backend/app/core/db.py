import sqlite3
from app.core.config import DATABASE_URL

DB_PATH = DATABASE_URL.replace("sqlite:///", "")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        job_id TEXT PRIMARY KEY,
        asset_id TEXT,
        scheduled_time TEXT,
        technician TEXT,
        status TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        job_id TEXT,
        outcome TEXT,
        resolved INTEGER,
        comments TEXT
    )
    """)

    conn.commit()
    conn.close()
