from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk




def open_add_order_window(parent, on_close_callback):
    add_window = Toplevel(parent)
    add_window.title("Добавить заказ")
    add_window.geometry("400x300")

    comboboxes = []

    #TODO: заменить на вызов с БД
    options = ["Выберите элемент", "Ремонт", "Установка","Диагностика"]

    Label(add_window, text="Количество принтеров").pack(pady=5)
    qty_entry = Entry(add_window)
    qty_entry.pack(pady=5)

    
    
    def add_combobox():
        combo = ttk.Combobox(frame, values=options)
        combo.pack(pady=5)
        comboboxes.append(combo)
    

    def save_order():
        selected_services = [cb.get() for cb in comboboxes if cb.get()]
        combined = ", ".join(selected_services)
        
        quantity = qty_entry.get()
        if not combined or not quantity.isdigit():
            messagebox.showerror("Ошибка", "Введите корректные данные")
            return
        conn = sqlite3.connect("databases/orders.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (item, quantity) VALUES (?, ?)", (combined, int(quantity)))
        conn.commit()
        conn.close()
        add_window.destroy()
        on_close_callback()

    frame = Frame(add_window)
    txt = Label(frame,text="Услуги")
    txt.pack(pady=10)
    frame.pack(pady=20)

    add_combobox()  # начальный комбо-бокс
    Button(add_window, text="Добавить услугу", command=add_combobox).pack(pady=10)
    Button(add_window, text="Сохранить", command=save_order).pack(pady=10)