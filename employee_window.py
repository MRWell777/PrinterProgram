from tkinter import Button, Toplevel, Label
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
from add_order import open_add_order_window
from edit_order import edit_selected_order



is_fullscreen = True  # Переменная для определения в каком состоянии находится в данный момент окно приложения (полноэкранный\оконный)


def open_employee_window(win,password_entry,username):
    

    win.withdraw()

    employee_window = Toplevel(win)
    employee_window.title("Личный кабинет пользователя")
    employee_window.geometry("400x300")
    employee_window.attributes('-fullscreen', True)

    windowed_size = "1366x768"  # Масштаб окна в оконном режиме

    image = Image.open("res/exit.png").convert("RGBA")  
    photo = ImageTk.PhotoImage(image)

    style = ttk.Style()
    style.theme_use("default")  # Используем тему по умолчанию
    
    screen_width = employee_window.winfo_screenwidth()
    screen_height = employee_window.winfo_screenheight()

    bg_image = Image.open("res/BackGroundUser.png")  # Укажите путь к изображению
    bg_image = bg_image.resize((screen_width, screen_height))  # Изменяем размер под экран
    bg_photo = ImageTk.PhotoImage(bg_image)

    photo_add = Image.open("res/add.png").convert("RGBA")
    resize_add = photo_add.resize((60,60))
    image_add = ImageTk.PhotoImage(resize_add)

    photo_edit = Image.open("res/edit.png")
    resize_edit = photo_edit.resize((60,60))
    image_edit = ImageTk.PhotoImage(resize_edit)

    photo_delete = Image.open("res/delete.png")
    resize_delete = photo_delete.resize((60,60))
    image_delete = ImageTk.PhotoImage(resize_delete)

    #сохранение данных
    employee_window.bg_photo = bg_photo 
    employee_window.photo = photo
    employee_window.image_add = image_add
    employee_window.image_edit = image_edit
    employee_window.image_delete = image_delete
    

    bg_label = Label(employee_window, image=employee_window.bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    
    

    # Загрузка изображения кнопки для выхода из оконного режима
    buttonSize = Image.open("res/Size.png").convert("RGBA")  
    buttonWidth = ImageTk.PhotoImage(buttonSize)

    # Загрузка изображения кнопки для выхода из полноэкранного режима
    buttonWindow = Image.open("res/ButtonWindow.png").convert("RGBA")  
    buttonWin = ImageTk.PhotoImage(buttonWindow)

    # Функция для определения полноэкранного режима
    def toggle_fullscreen():
        global is_fullscreen
        is_fullscreen = not is_fullscreen  # Переключаем флаг
        if is_fullscreen:
            employee_window.attributes('-fullscreen', True)  # Включаем полный экран
            toggle_button.config(image = buttonWin)
        else:
            employee_window.attributes('-fullscreen', False)  # Отключаем полный экран 
            employee_window.geometry(windowed_size)  # Устанавливаем фиксированный размер окна
            toggle_button.config(image = buttonWidth)

    def go_back():
        password_entry.delete(0, 'end')
        employee_window.destroy()         # закрываем личный кабинет
        win.deiconify()     # возвращаем главное окно

   

    Button(employee_window,image=photo,bg="#000213",bd = 0, command=go_back).place(x=30, y=700)

    
    bottom_frame = Label(employee_window, bg="#000421")
    bottom_frame.pack(anchor="se",side="bottom", pady=10,padx=350)

    # Кнопка "Добавить"
    add_button = Button(bottom_frame, image=image_add, bg="#000421", bd=0,
                    command=lambda: open_add_order_window(employee_window, refresh_orders))
    add_button.pack(side="left", padx=10)

    # Кнопка "Редактировать"
    edit_button = Button(bottom_frame, image=image_edit, bg="#000421", bd=0,
                     command=lambda: edit_selected_order(employee_window, orders_tree, refresh_orders))
    edit_button.pack(side="left", padx=10)

    def delete_order(tree, refresh_callback):
        selected = tree.focus()
        if not selected:
            messagebox.showwarning("Нет выбора", "Выберите заказ для удаления")
            return

        values = tree.item(selected, "values")
        order_id = values[0]

        confirm = messagebox.askyesno("Подтверждение", f"Удалить заказ с ID {order_id}?")
        if confirm:
            conn = sqlite3.connect("databases/orders.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
            conn.commit()
            conn.close()
            refresh_callback()

    def on_right_click(event):
        row_id = orders_tree.identify_row(event.y)
        if row_id:
            orders_tree.selection_set(row_id)  # выделяем строку под курсором
            delete_order(orders_tree, refresh_orders)
        

    delete_button = Button(bottom_frame, image=image_delete, bg="#000421", bd=0, command=lambda: delete_order(orders_tree, refresh_orders))
    delete_button.pack(side="left", padx=10)

    # Кнопка расширения экрана
    toggle_button = Button(employee_window, image = buttonWin, bg="#000213", bd = 0, command=toggle_fullscreen)
    toggle_button.pack(anchor="ne")
    toggle_button.config(cursor="hand2")

    

# Настройка цветов таблицы
    style.configure("Treeview",
                background="#135f82",     # Цвет фона строк
                foreground="white",       # Цвет текста строк
                fieldbackground="#135f82",# Фон пустого пространства
                rowheight=25,font=("v_CCMeanwhile", 10, "bold"))

# Цвет при выделении строки
    style.map("Treeview",
          background=[('selected', '#104c68')],
          foreground=[('selected', 'white')])
    
    style.configure("Treeview.Heading",
                background="#125978",    # Фон заголовка
                foreground="white",      # Цвет текста заголовка
                font=("v_CCMeanwhile", 10, "bold"))  # Шрифт заголовка
    
    

    

    # Список заказов
    orders_tree = ttk.Treeview(employee_window, columns=("id", "item", "quantity"), show="headings")
    orders_tree.heading("id", text="ID")
    orders_tree.column("id", width=50, anchor='center')

    orders_tree.heading("item", text="Товар")
    orders_tree.column("item", width=150)

    orders_tree.heading("quantity", text="Количество")
    orders_tree.column("quantity", width=100, anchor='center')

    orders_tree.place(x=800, y=300, width=500, height=300)

    orders_tree.bind("<Double-1>", lambda event: edit_selected_order(employee_window,orders_tree, refresh_orders))
    orders_tree.bind("<Button-3>", lambda event: on_right_click(event))

    def refresh_orders():
        for row in orders_tree.get_children():
            orders_tree.delete(row)
        conn = sqlite3.connect("databases/orders.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, item, quantity FROM orders ")
        for row in cursor.fetchall():
            orders_tree.insert("", "end", values=row)
        conn.close()

    refresh_orders()