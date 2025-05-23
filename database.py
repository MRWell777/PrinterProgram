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
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('emp1', '1', 'employee')")
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('emp2', '2', 'employee')")
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('admin', '123', 'admin')")
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('user1', '1', 'user')")
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('user2', '2', 'user')")

    conn.commit()
    conn.close()

# Запускаем инициализацию базы
init_db()
