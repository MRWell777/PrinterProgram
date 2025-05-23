from tkinter import Button, Toplevel, Label
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
from questionnaire_user import open_quest_user


is_fullscreen = True  # Переменная для определения в каком состоянии находится в данный момент окно приложения (полноэкранный\оконный)


def open_user_window(win,password_entry,username):
    

    win.withdraw()

    user_window = Toplevel(win)
    user_window.title("Личный кабинет пользователя")
    user_window.geometry("400x300")
    user_window.attributes('-fullscreen', True)

    print("пользователь",username)

    windowed_size = "1366x768"  # Масштаб окна в оконном режиме

    image = Image.open("res/exit.png").convert("RGBA")  
    photo = ImageTk.PhotoImage(image)

    style = ttk.Style()
    style.theme_use("default")  # Используем тему по умолчанию
    
    screen_width = user_window.winfo_screenwidth()
    screen_height = user_window.winfo_screenheight()

    bg_image = Image.open("res/userBG.png")  # Укажите путь к изображению
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
    user_window.bg_photo = bg_photo 
    user_window.photo = photo
    user_window.image_add = image_add
    user_window.image_edit = image_edit
    user_window.image_delete = image_delete
    

    bg_label = Label(user_window, image=user_window.bg_photo)
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
            user_window.attributes('-fullscreen', True)  # Включаем полный экран
            toggle_button.config(image = buttonWin)
        else:
            user_window.attributes('-fullscreen', False)  # Отключаем полный экран 
            user_window.geometry(windowed_size)  # Устанавливаем фиксированный размер окна
            toggle_button.config(image = buttonWidth)

    def go_back():
        password_entry.delete(0, 'end')
        user_window.destroy()         # закрываем личный кабинет
        win.deiconify()     # возвращаем главное окно

   

    Button(user_window,image=photo,bg="#000213",bd = 0, command=go_back).place(x=30, y=700)

    
    
    bottom_frame = Label(user_window, bg="#000421")
    bottom_frame.pack(anchor="se",side="bottom", pady=10,padx=500)

    txt = Label(bottom_frame,text="ПУСТО",fg="white",font=("v_CCMeanwhile",30),bg="#000421")
    txt.pack(anchor="center", pady=300)

    # Кнопка "Добавить"
    add_button = Button(bottom_frame, image=image_add, bg="#000421", bd=0,command=lambda:open_quest_user(user_window,username))
    add_button.pack(side="left", padx=10)

    # Кнопка "Редактировать"
    edit_button = Button(bottom_frame, image=image_edit, bg="#000421", bd=0)
    edit_button.pack(side="left", padx=10)     

    delete_button = Button(bottom_frame, image=image_delete, bg="#000421", bd=0)
    delete_button.pack(side="left", padx=10)

    # Кнопка расширения экрана
    toggle_button = Button(user_window, image = buttonWin, bg="#000213", bd = 0, command=toggle_fullscreen)
    toggle_button.pack(anchor="ne")
    toggle_button.config(cursor="hand2")

    


    
    
        

    

    