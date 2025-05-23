from tkinter import *
import sqlite3
from tkinter import messagebox

def edit_selected_order(parent, tree, on_close_callback):
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Нет выбора", "Выберите заказ для редактирования")
        return

    values = tree.item(selected, "values")
    order_id, item, qty = values

    edit_window = Toplevel(parent)
    edit_window.title("Редактировать заказ")
    edit_window.geometry("400x300")

    Label(edit_window, text="Товар").pack(pady=5)
    item_entry = Entry(edit_window)
    item_entry.insert(0, item)
    item_entry.pack(pady=5)

    Label(edit_window, text="Количество").pack(pady=5)
    qty_entry = Entry(edit_window)
    qty_entry.insert(0, qty)
    qty_entry.pack(pady=5)

    def hide_tree():
        tree.place_forget()  # Или orders_tree.destroy()

    Button(edit_window, text="Скрыть таблицу", command=hide_tree).pack(pady=20)

    

    

    

    def update_order():
        new_item = item_entry.get()
        new_qty = qty_entry.get()
        if not new_item or not new_qty.isdigit():
            messagebox.showerror("Ошибка", "Введите корректные данные")
            return
        conn = sqlite3.connect("orders.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE orders SET item = ?, quantity = ? WHERE id = ?", (new_item, int(new_qty), order_id))
        conn.commit()
        conn.close()
        edit_window.destroy()
        on_close_callback()

    Button(edit_window, text="Сохранить", command=update_order).pack(pady=20)