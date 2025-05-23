import sqlite3

conn = sqlite3.connect("statuses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS statuses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
""")

# Добавим статусы, если ещё нет
for status in ["Ожидает", "Принят", "Выполнен"]:
    cursor.execute("INSERT OR IGNORE INTO statuses (name) VALUES (?)", (status,))

conn.commit()
conn.close()