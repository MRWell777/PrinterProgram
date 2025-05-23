from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox


window = Tk()
window.geometry("400x400")

services = ["Стрижка", "Маникюр", "Массаж", "Укладка"]  # список услуг
comboboxes = []  # список всех добавленных комбобоксов

Label(window, text="Количество принтеров").pack(pady=5)
qty_entry = Entry(window)
qty_entry.pack(pady=5)

# === Функция добавления нового комбобокса ===
def add_combobox():
    combo = ttk.Combobox(frame, values=services)
    combo.pack(pady=5)
    comboboxes.append(combo)

# === Функция сохранения в БД ===
def save_services():
    selected_services = [cb.get() for cb in comboboxes if cb.get()]
    combined = ", ".join(selected_services)
    quantity = qty_entry.get()
    if not quantity.isdigit():
            messagebox.showerror("Ошибка", "Введите корректные данные")
            return
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (item,quantity) VALUES (?, ?)", (combined,))
    conn.commit()
    conn.close()

    print("Сохранено:", combined)

# === Интерфейс ===
frame = Frame(window)
txt = Label(text="Услуги")
txt.pack(pady=10)
frame.pack(pady=20)

add_combobox()  # начальный комбобокс

Button(window, text="Добавить услугу", command=add_combobox).pack(pady=10)
Button(window, text="Сохранить в БД", command=save_services).pack(pady=10)

window.mainloop()