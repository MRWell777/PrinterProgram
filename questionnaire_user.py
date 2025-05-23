from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

def open_quest_user(parent,username):
    quest_user = Toplevel(parent)
    quest_user.title("Анкета")
    quest_user.overrideredirect(True)

    # Размер окна
    win_width = 700
    win_height = 600

    # Получаем размеры экрана
    screen_width = quest_user.winfo_screenwidth()
    screen_height = quest_user.winfo_screenheight()

    

    # Вычисляем координаты для центрирования
    x = (screen_width // 2) - (win_width // 2) + 150
    y = (screen_height // 2) - (win_height // 2)

    # Устанавливаем геометрию по центру
    quest_user.geometry(f"{win_width}x{win_height}+{x}+{y}")

    # Загружаем и изменяем фон под размер окна
    bg_image = Image.open("res/quest_bg.png")
    bg_image = bg_image.resize((win_width, win_height))  # под размер окна
    bg_photo = ImageTk.PhotoImage(bg_image)

    line_image = Image.open("res/Line_acua_blue.png")
    line_image = line_image.resize((250,35))
    Line_photo = ImageTk.PhotoImage(line_image)

    menu_line_image = Image.open("res/Line_acua_blue.png")
    menu_line_image = menu_line_image.resize((300,35))
    menu_line_photo = ImageTk.PhotoImage(menu_line_image)

    add_image = Image.open("res/add_image.png")
    add_image=add_image.resize((20,20))
    add_photo = ImageTk.PhotoImage(add_image)

    trash_image = Image.open("res/trash_image.png")
    trash_image=trash_image.resize((20,20))
    trash_photo = ImageTk.PhotoImage(trash_image)

    quest_user.bg_photo = bg_photo  # чтобы изображение не удалилось сборщиком мусора
    quest_user.Line_photo = Line_photo
    quest_user.add_photo = add_photo
    quest_user.trash_photo = trash_photo
    quest_user.menu_line_photo = menu_line_photo

    bg_label = Label(quest_user, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    menu_underline = Label(quest_user, image=menu_line_photo, bg="#000421")
    

    fields = {
        "Фамилия:": None,
        "Имя:": None,
        "Отчество:": None,
        "Город:": None,
        "Улица:": None,
        "Дом:": None,
        "Подъезд:": None,
        "Кол-во принтеров:": None,
        "Номер телефона:": None,
        "Почта:": None
        
    }

    y_offset = 50
    for label_text in fields:
        label = Label(quest_user, text=label_text,fg="white", bg="#000421", font=("v_CCMeanwhile", 10, "bold"))
        label.place(x=30, y=y_offset+9)

        underline = Label(quest_user, image=Line_photo, bg="#000421")
        underline.place(x=245, y=y_offset)

        entry = Entry(quest_user,bg="#115d81",relief="flat", width=20,fg="white",font=("v_CCMeanwhile", 10, "bold"))
        entry.place(x=259, y=y_offset +9)
        fields[label_text] = entry
        y_offset += 40

        

    
    # ---------- Надпись "Услуги" ----------
    Label(quest_user, text="Услуги:", bg="#000421", fg="white", font=("v_CCMeanwhile", 10, "bold")).place(x=30, y=y_offset + 9)

    # ---------- Услуги (OptionMenus с ограничением) ----------
    service_options = ["Ремонт", "Установка", "Диагностика"]
    option_widgets = []

    def get_used_services():
        return [var.get() for _, var, _ in option_widgets if var.get() != "Выберите услугу"]

    def update_menus():
        used = get_used_services()
        for frame, var, _ in option_widgets:
            menu = frame.option_menu["menu"]
            menu.delete(0, "end")
            for option in service_options:
                if option not in used or var.get() == option:
                    menu.add_command(label=option, command=lambda v=var, o=option: v.set(o))

    def reposition_widgets():
        for index, (frame, var, menu_underline) in enumerate(option_widgets):
            for widget in frame.winfo_children():
                widget.destroy()
            
            option_menu = OptionMenu(frame, var, *service_options)
            option_menu.config(bg="#115d81", fg="white", font=("v_CCMeanwhile", 10, "bold"),
                               activebackground="#444", activeforeground="white",
                               width=17, borderwidth=0, highlightthickness=0)
            option_menu["menu"].config(bg="#115d81", fg="white", font=("v_CCMeanwhile", 10, "bold"))
            option_menu.pack(side=LEFT)
            frame.option_menu = option_menu

            if index == 0:
                Button(frame, image=quest_user.add_photo,bg="#115d81", activebackground="#115d81", 
                       bd=0, command=add_option_menu).pack(side=LEFT,padx=10)
            else:
                Button(frame, image=quest_user.trash_photo,bg="#115d81", activebackground="#115d81", 
                       bd=0, command=lambda f=frame: remove_option_menu(f)).pack(side=LEFT, padx=10)

            y_pos = y_offset + 7 + index * 40

            # ====== Показываем подчеркивание ======
            menu_underline.place(x=245, y=y_pos )
            menu_underline.lift()  # 👈 гарантированно над фоном
            frame.lift()      # 👈 и над линией, но ниже option_menu

            
            frame.place(x=260, y=y_pos+7)
            

        update_menus()

    def add_option_menu():
        if len(option_widgets) >= 3:
            messagebox.showinfo("Ограничение", "Можно выбрать не более 3 услуг")
            return
        var = StringVar(value="Выберите услугу")
        frame = Frame(quest_user, bg="#115d81")
        menu_underline = Label(quest_user, image=menu_line_photo, bg="#000421")
        option_widgets.append((frame, var, menu_underline))
        reposition_widgets()

    def remove_option_menu(frame_to_remove):
        if len(option_widgets) <= 1:
            messagebox.showinfo("Ограничение", "Хотя бы одна услуга должна остаться")
            return
        for i, (frame, var, menu_underline) in enumerate(option_widgets):
            if frame == frame_to_remove:
                option_widgets.pop(i)
                frame.destroy()
                menu_underline.destroy()
                break
        reposition_widgets()

    # Первый элемент сразу
    add_option_menu()

    from datetime import datetime

    def save_order():
        # 1. Собираем данные
        data = {label: entry.get() for label, entry in fields.items()}

        # Проверка (добавь при необходимости)
        if not data["Фамилия:"] or not data["Имя:"] or not data["Номер телефона:"]:
            messagebox.showerror("Ошибка", "Пожалуйста, заполните обязательные поля")
            return

        # 2. Услуги
        ## TODO: заменить код загрузки услуг на вызов с БД
        selected_services = [var.get() for _, var, _ in option_widgets if var.get() != "Выберите услугу"]
        if not selected_services:
            messagebox.showerror("Ошибка", "Выберите хотя бы одну услугу.")
            return
        services_str = ", ".join(selected_services)

        # 3. Дата
        today = datetime.now().strftime("%Y-%m-%d")

        # 4. Получаем ID статуса "Ожидает"
        try:
            status_conn = sqlite3.connect("statuses.db")
            status_cursor = status_conn.cursor()
            status_cursor.execute("SELECT id FROM statuses WHERE name = ?", ("Ожидает",))
            status_id = status_cursor.fetchone()[0]
            status_conn.close()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при получении статуса: {e}")
            return

            # 5. Сохраняем в orders.db
        try:
            order_conn = sqlite3.connect("order.db")
            order_cursor = order_conn.cursor()
            order_cursor.execute("""
            INSERT INTO orders (
                last_name, first_name, middle_name, city, street, house,
                entrance, printer_count, phone, email, services, date_created, status_id, username
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
            data["Фамилия:"], data["Имя:"], data["Отчество:"],
            data["Город:"], data["Улица:"], data["Дом:"],
            int(data["Подъезд:"]) if data["Подъезд:"].isdigit() else None,
            int(data["Кол-во принтеров:"]) if data["Кол-во принтеров:"].isdigit() else None,
            data["Номер телефона:"], data["Почта:"],
            services_str, today, status_id,username
            ))
            order_conn.commit()

            # Получаем ID заказа
            order_id = order_cursor.lastrowid
            order_conn.close()

            messagebox.showinfo("Заказ сохранён", f"Заказ успешно сохранён.\nID заказа: {order_id}")
            quest_user.destroy()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при сохранении заказа: {e}")
        
        

    Button(quest_user, text="Сохранить", bg="#115d81", fg="white", font=("v_CCMeanwhile", 10, "bold"),
       command=save_order).place(x=50, y=520)
    
   