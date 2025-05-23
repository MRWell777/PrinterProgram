from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk
import ctypes
from user_window import open_user_window
from admin_window import open_admin_window
from employee_window import open_employee_window


window = Tk()

window.title("Главная страница") # Название страницы

window.iconbitmap('res/icon.ico') # Иконка приложения

window.attributes('-fullscreen', True) # Установка окна в полноэкранный режим

is_fullscreen = True  # Переменная для определения в каком состоянии находится в данный момент окно приложения (полноэкранный\оконный)

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
        window.attributes('-fullscreen', True)  # Включаем полный экран
        toggle_button.config(image = buttonWin)
    else:
        window.attributes('-fullscreen', False)  # Отключаем полный экран 
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Устанавливаем фиксированный размер окна и размещаем в центре экрана
        window.resizable(False,False)
        toggle_button.config(image = buttonWidth)

# Получение данных о соотношении сторон экрана
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Данные об окне
window_width = 550
window_height = 480

# Подсчет по осям x и y для расположения окна по центру экрана
x = int(int(screen_width/2) - int(window_width/2))
y = int(int(screen_height/2) - int(window_height/2))

# Загрузка изображени для заднего фона
bg_image = Image.open("res/BackGround.png")  
bg_image = bg_image.resize((screen_width, screen_height))  # Изменяем размер под экран
bg_photo = ImageTk.PhotoImage(bg_image)

# Загрузка изображени для кнопки закрытия приложения
image = Image.open("res/x.png").convert("RGBA")  
photo = ImageTk.PhotoImage(image)

# Загрузка изображени для кнопки входа
vhod = Image.open("res/button_vhod.png").convert("RGBA")  
resized_image = vhod.resize((int(vhod.width * 0.7), int(vhod.height * 0.7)))
imagevhod = ImageTk.PhotoImage(resized_image)

# Загрузка изображени для строки логина
loginpng = Image.open("res/LoginLine.png").convert("RGBA")
resized_image_log = loginpng.resize((int(loginpng.width * 0.65), int(loginpng.height * 0.65)))  
loginimage = ImageTk.PhotoImage(resized_image_log)

# Загрузка изображени для строки пароля
passwordimageline = Image.open("res/PasswordLine.png").convert("RGBA")
resized_image_pas = passwordimageline.resize((int(passwordimageline.width * 0.65), int(passwordimageline.height * 0.65)))  
passwordimage = ImageTk.PhotoImage(resized_image_pas)

# Изображение пользователя
iconimage = Image.open("res/Icon.png").convert("RGBA")
resized_image_ico = iconimage.resize((int(iconimage.width * 0.65), int(iconimage.height * 0.65)))  
icoimage = ImageTk.PhotoImage(resized_image_ico)

# Функция для проверки CapsLock
def check_caps_lock(event=None):
    caps_on = ctypes.WinDLL("User32.dll").GetKeyState(0x14)
    if caps_on:
        caps_label.config(text="⚠️ CAPS LOCK ВКЛЮЧЕН", fg="white", font=("v_CCMeanwhile",14))
    else:
        caps_label.config(text="")

# Фон
bg_label = Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Задаем frame для отрисовки всех функциональных объектов
frame = Frame(window, bg="#000c25", width=screen_width, height=screen_height)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Иконка
Label(frame, image=icoimage, bg="#000c25", bd=0).pack(pady=5)

# Логин
Label(frame, image=loginimage, bg="#000c25", bd=0).pack(pady=5)

# Пароль
Label(frame, image=passwordimage, bg="#000c25", bd=0).pack(pady=5)

# Фокусировка на пароль
def focus_password(event):
    password_entry.focus_set()

# Строка ввода Логина
login_entry = Entry(frame, width=15, bg="#115d81", fg="white", relief="flat", font = ("v_CCMeanwhile",14))
login_entry.place(relx=0.65, rely=0.485, anchor="center")
login_entry.bind("<KeyRelease>", check_caps_lock)
login_entry.bind("<Return>", focus_password)

# Строка ввода пароля
password_entry = Entry(frame, width=15,bg="#115d81", fg="white", relief="flat", font = ("v_CCMeanwhile",14), show="*")
password_entry.place(relx=0.7, rely=0.625, anchor="center")
password_entry.bind("<KeyRelease>",check_caps_lock)
password_entry.bind("<Return>", lambda event: check_login())

# Проверка на правильность логина и пароля
def check_login():
   
    username = login_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        role = user[0]
        
        if role == "admin":
            open_admin_window(window,password_entry,username)
        elif role == "employee":
            open_employee_window(window,password_entry,username)
        else:
            open_user_window(window,password_entry,username)
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")

# Кнопка Входа
button_login = Button(frame, image=imagevhod, bg="#000c25", bd = 0, command=check_login)
button_login.pack(pady=10)
button_login.config(cursor="hand2")

# Текст который высвечивается когда нажат capslock
caps_label = Label(frame, text="", font=("v_CCMeanwhile",14), bg="#000c25")
caps_label.pack(pady=10)

# Кнопка Выхода
button_exit = Button(window, image=photo, bg="#000213", bd = 0, command=window.destroy)  # Цвет фона можно изменить
button_exit.pack(anchor=NE)
button_exit.config(cursor="hand2")

# Кнопка расширения экрана
toggle_button = Button(window, image = buttonWin, bg="#000213", bd = 0, command=toggle_fullscreen)
toggle_button.pack(anchor=NE)
toggle_button.config(cursor="hand2")

# Запуск приложения
window.mainloop()