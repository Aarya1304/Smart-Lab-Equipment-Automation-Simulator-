import sqlite3

def init_db():
    """
    Initializes the SQLite database.
    Creates a machine_logs table to store
    machine commands and their responses.
    """

    conn = sqlite3.connect("lab.db")
    cursor = conn.cursor()

    # Table stores command history for traceability
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS machine_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            command TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()