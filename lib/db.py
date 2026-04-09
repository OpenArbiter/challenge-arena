"""Database access layer."""
import sqlite3


def get_user(db_path: str, username: str) -> dict | None:
    """Look up a user by username."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # SQL injection — user input directly in query
    cursor.execute(f"SELECT * FROM users WHERE name = '{username}'")
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None
