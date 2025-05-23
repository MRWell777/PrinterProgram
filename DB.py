import sqlite3

## Создаём базу данных и коннект к ней, чтобы создать таблицу, если её нет
## Правда не совсем понятно, почему только одну, но бог с ним
conn = sqlite3.connect("databases/orders.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT,
        quantity INTEGER
    )
""")
conn.commit()
conn.close()