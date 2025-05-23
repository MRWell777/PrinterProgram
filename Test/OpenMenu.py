from tkinter import *
from tkinter import messagebox

def open_quest_user():
    root = Toplevel()
    root.title("Анкета")
    root.geometry("600x400")

    services = ["Ремонт", "Установка", "Диагностика"]
    option_widgets = []  # [(frame, var)]
    selected_values = set()

    def update_all_option_menus():
        for frame, var in option_widgets:
            current = var.get()
            menu = frame.option_menu["menu"]
            menu.delete(0, "end")
            for service in services:
                if service not in selected_values or service == current:
                    menu.add_command(label=service, command=lambda v=var, val=service: on_select(v, val))

    def on_select(var, value):
        old_value = var.get()
        if old_value in selected_values:
            selected_values.remove(old_value)
        var.set(value)
        selected_values.add(value)
        update_all_option_menus()

    def remove_option_menu(frame, var):
        if len(option_widgets) <= 1:
            messagebox.showwarning("Ограничение", "Хотя бы один пункт услуги должен остаться.")
            return

        value = var.get()
        if value in selected_values:
            selected_values.remove(value)

        option_widgets.remove((frame, var))
        frame.destroy()
        reposition_widgets()
        update_all_option_menus()

    def reposition_widgets():
        for index, (frame, var) in enumerate(option_widgets):
            for widget in frame.winfo_children():
                widget.destroy()

            option_menu = OptionMenu(frame, var, *services)
            option_menu.config(bg="#115d81", fg="white", font=("Arial", 10), highlightthickness=0)
            option_menu.pack(side=LEFT)
            frame.option_menu = option_menu

            if index == 0:
                # Первая строка — только кнопка "Добавить"
                btn_add = Button(frame, text="Добавить услугу", command=add_option_menu)
                btn_add.pack(side=LEFT, padx=10)
            else:
                # Остальные — кнопка "Удалить"
                btn_del = Button(frame, text="Удалить", command=lambda f=frame, v=var: remove_option_menu(f, v))
                btn_del.pack(side=LEFT, padx=10)

            frame.place(x=50, y=50 + index * 50)


    def add_option_menu():
        if len(option_widgets) >= 3:
            messagebox.showinfo("Ограничение", "Можно выбрать максимум 3 разные услуги.")
            return

        frame = Frame(root, bg="#000421")
        var = StringVar(value="Выберите услугу")

        option_menu = OptionMenu(frame, var, *services)
        option_menu.config(bg="#115d81", fg="white", font=("Arial", 10), highlightthickness=0)
        option_menu.pack(side=LEFT)

        frame.option_menu = option_menu  # сохранить ссылку для обновления

        btn_del = Button(frame, text="Удалить", command=lambda f=frame, v=var: remove_option_menu(f, v))
        btn_del.pack(side=LEFT, padx=10)

        option_widgets.append((frame, var))
        reposition_widgets()  # пересчитать все позиции после добавления
        update_all_option_menus()

    add_option_menu()

    