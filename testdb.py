import sqlite3
from tkinter import *
from tkinter import ttk

# Создаем отдельное окно
root = Tk()
root.title("Просмотр базы заказов")
root.geometry("1500x500")
root.configure(bg="#000421")

# Подключение к двум базам данных
conn = sqlite3.connect("order.db")
conn.execute("ATTACH DATABASE 'statuses.db' AS status_db")
conn.execute("ATTACH DATABASE 'users.db' AS username")
cursor = conn.cursor()

# Получение всех заказов с расшифровкой статуса
cursor.execute("""
SELECT 
    o.id,
    o.last_name,
    o.first_name,
    o.middle_name,
    o.city,
    o.street,
    o.house,
    o.entrance,
    o.printer_count,
    o.phone,
    o.email,
    o.services,
    o.date_created,
    s.name as status_name,
    u.username AS user_login
FROM orders o
JOIN status_db.statuses s ON o.status_id = s.id
LEFT JOIN username.users u ON o.username = u.username
ORDER BY o.id DESC
""")

rows = cursor.fetchall()

# Колонки таблицы
columns = [
    "ID", "Фамилия", "Имя", "Отчество", "Город", "Улица", "Дом", "Подъезд",
    "Принтеры", "Телефон", "Почта", "Услуги", "Дата", "Статус","Логин"
]

# Создание Treeview
tree = ttk.Treeview(root, columns=columns, show="headings")

# Установка заголовков и размеров
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor=CENTER)

# Вставка строк
for row in rows:
    tree.insert("", END, values=row)

tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Запуск окна
root.mainloop()

# Закрытие соединения
conn.close()
