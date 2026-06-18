import sqlite3


DB_NAME = "memory/startup_memory.db"


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

    return row[0]

def get_startup_count():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM startups"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count

