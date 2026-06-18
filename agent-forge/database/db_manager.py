import sqlite3
from pathlib import Path


# ------------------------------------
# Ensure Memory Folder Exists
# ------------------------------------

Path("memory").mkdir(
    parents=True,
    exist_ok=True
)

DB_NAME = "memory/startup_memory.db"


# ------------------------------------
# Initialize Database
# ------------------------------------

def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS startups (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            idea TEXT,

            report TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    conn.close()


# ------------------------------------
# Save Startup
# ------------------------------------

def save_startup(
    idea,
    report
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO startups
        (
            idea,
            report
        )
        VALUES (?, ?)
        """,
        (
            idea,
            report
        )
    )

    conn.commit()
    conn.close()


# ------------------------------------
# Get All Startups
# ------------------------------------

def get_all_startups():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            idea,
            created_at
        FROM startups
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


# ------------------------------------
# Get Single Report
# ------------------------------------

def get_startup_report(
    startup_id
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT report
        FROM startups
        WHERE id = ?
        """,
        (startup_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return "No report found."


# ------------------------------------
# Startup Counter
# ------------------------------------

def get_startup_count():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM startups"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count
