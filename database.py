import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Создаём таблицу пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    # Добавляем пользователей (если их нет)
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('user1', 'password123', 'user')")
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('admin', 'adminpass', 'admin')")

    conn.commit()
    conn.close()

# Запускаем инициализацию базы
init_db()
