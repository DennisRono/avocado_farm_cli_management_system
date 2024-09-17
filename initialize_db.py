from main import cursor, conn, current_date


# Create tables if they don't already exist
def initialize_db():
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS trees (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tree_id TEXT,
                        height REAL,
                        leaf_health TEXT,
                        date TEXT)"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS irrigation (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tree_id TEXT,
                        volume REAL,
                        duration REAL,
                        date TEXT)"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS harvest (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tree_id TEXT,
                        quantity REAL,
                        date TEXT)"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS inventory (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        quantity REAL,
                        size TEXT,
                        quality TEXT,
                        date TEXT)"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        category TEXT,
                        amount REAL,
                        description TEXT,
                        date TEXT)"""
    )

    conn.commit()
