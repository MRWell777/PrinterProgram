import sqlite3

conn = sqlite3.connect("order.db")
cursor = conn.cursor()

# Создаем таблицу статусов
cursor.execute("""
CREATE TABLE IF NOT EXISTS statuses (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
INSERT OR IGNORE INTO statuses (id, name) VALUES
(1, 'Ожидание'),
(2, 'Принят'),
(3, 'Выполнен')
""")

# Создаем таблицу заказов
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
    phone_number INTEGER,
    email TEXT,
    service TEXT,
    date_created TEXT,
    status_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES statuses(id)
)
""")

conn.commit()
conn.close()