from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk
import ctypes



window = Tk()




window.title("ЮДЖИНПРИНТ")

windowed_size = "1366x768"  

window.attributes('-fullscreen', True)

is_fullscreen = True  

buttonSize = Image.open("res/Size.png").convert("RGBA")  
buttonWidth = ImageTk.PhotoImage(buttonSize)

buttonWindow = Image.open("res/ButtonWindow.png").convert("RGBA")  
buttonWin = ImageTk.PhotoImage(buttonWindow)

def toggle_fullscreen():
    global is_fullscreen
    is_fullscreen = not is_fullscreen  # Переключаем флаг
    if is_fullscreen:
        window.attributes('-fullscreen', True)  # Включаем полный экран
        toggle_button.config(image = buttonWin)
    else:
        window.attributes('-fullscreen', False)  # Отключаем полный экран
        window.geometry(windowed_size)  # Устанавливаем фиксированный размер окна
        toggle_button.config(image = buttonWidth)

window.iconbitmap('res/icon.ico')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

bg_image = Image.open("res/BackGround.png")  # Укажите путь к изображению
bg_image = bg_image.resize((screen_width, screen_height))  # Изменяем размер под экран
bg_photo = ImageTk.PhotoImage(bg_image)


image = Image.open("res/x.png").convert("RGBA")  
photo = ImageTk.PhotoImage(image)

vhod = Image.open("res/button_vhod.png").convert("RGBA")  
resized_image = vhod.resize((int(vhod.width * 0.7), int(vhod.height * 0.7)))
imagevhod = ImageTk.PhotoImage(resized_image)


loginpng = Image.open("res/LoginLine.png").convert("RGBA")
resized_image_log = loginpng.resize((int(loginpng.width * 0.65), int(loginpng.height * 0.65)))  
loginimage = ImageTk.PhotoImage(resized_image_log)

passwordimageline = Image.open("res/PasswordLine.png").convert("RGBA")
resized_image_pas = passwordimageline.resize((int(passwordimageline.width * 0.65), int(passwordimageline.height * 0.65)))  
passwordimage = ImageTk.PhotoImage(resized_image_pas)

iconimage = Image.open("res/Icon.png").convert("RGBA")
resized_image_ico = iconimage.resize((int(iconimage.width * 0.65), int(iconimage.height * 0.65)))  
icoimage = ImageTk.PhotoImage(resized_image_ico)

def check_caps_lock(event=None):
    # Используем ctypes для Windows
    caps_on = ctypes.WinDLL("User32.dll").GetKeyState(0x14)
    if caps_on:
        caps_label.config(text="⚠️ CAPS LOCK ВКЛЮЧЕН", fg="white", font=("v_CCMeanwhile",14))
    else:
        caps_label.config(text="")


bg_label = Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)



frame = Frame(window, bg="#000c25", width=screen_width, height=screen_height)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

Label(frame, image=icoimage, bg="#000c25", bd=0).pack(pady=5)

Label(frame, image=loginimage, bg="#000c25", bd=0).pack(pady=5)

login_entry = Entry(frame, width=15, bg="#115d81", fg="white", relief="flat", font = ("v_CCMeanwhile",14))
login_entry.place(relx=0.65, rely=0.485, anchor="center")
#login_entry.pack(pady=5)
login_entry.bind("<KeyRelease>", check_caps_lock)



Label(frame, image=passwordimage, bg="#000c25", bd=0).pack(pady=5)

password_entry = Entry(frame, width=15,bg="#115d81", fg="white", relief="flat", font = ("v_CCMeanwhile",14), show="*")
password_entry.place(relx=0.7, rely=0.625, anchor="center")
#password_entry.pack(pady=5)
password_entry.bind("<KeyRelease>",check_caps_lock)




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
            open_admin_window()
        else:
            open_user_window()
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")


def open_user_window():
    user_window = Toplevel(window)
    user_window.title("Личный кабинет пользователя")
    #user_window.geometry("400x300")
    user_window.attributes('-fullscreen', True)
    Label(user_window, text="Добро пожаловать, пользователь!", font=("Arial", 14)).pack(pady=20)


def open_admin_window():
    admin_window = Toplevel(window)
    admin_window.title("Панель администратора")
    admin_window.geometry("400x300")
    Label(admin_window, text="Добро пожаловать, администратор!", font=("Arial", 14)).pack(pady=20)

button_login = Button(frame, image=imagevhod, bg="#000c25", bd = 0, command=check_login)
button_login.pack(pady=10)
button_login.config(cursor="hand2")

caps_label = Label(frame, text="", font=("v_CCMeanwhile",14), bg="#000c25")
caps_label.pack(pady=10)

button_exit = Button(window, image=photo, bg="#000213", bd = 0, command=window.destroy)  # Цвет фона можно изменить
button_exit.pack(anchor=NE)
button_exit.config(cursor="hand2")

toggle_button = Button(window, image = buttonWin, bg="#000213", bd = 0, command=toggle_fullscreen)
toggle_button.pack(anchor=NE)
toggle_button.config(cursor="hand2")

window.mainloop()