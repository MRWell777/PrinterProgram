import sqlite3

conn = sqlite3.connect("databases/order.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name TEXT,
    first_name TEXT,
    middle_name TEXT,
    city TEXT,
    street TEXT,
    house TEXT,
    entrance INTEGER,
    printer_count INTEGER,
    phone TEXT,
    email TEXT,
    services TEXT,
    date_created TEXT,
    status_id INTEGER,
    username TEXT
)
""")

conn.commit()
conn.close()
