from tkinter import Toplevel, Label, Button
from PIL import Image, ImageTk

# Если не используется, нахуя сюда его передавать?
def open_admin_window(win, password_entry):
    admin_window = Toplevel(win)
    admin_window.title("Личный кабинет пользователя")
    admin_window.geometry("400x300")
    admin_window.attributes('-fullscreen', True)
    
    screen_width = admin_window.winfo_screenwidth()
    screen_height = admin_window.winfo_screenheight()

    image = Image.open("res/exit.png").convert("RGBA")  
    photo = ImageTk.PhotoImage(image)

    bg_image = Image.open("res/AdminWindow.png")  # Укажите путь к изображению
    bg_image = bg_image.resize((screen_width, screen_height))  # Изменяем размер под экран
    bg_photo = ImageTk.PhotoImage(bg_image)

    admin_window.bg_photo = bg_photo #сохранение данных
    admin_window.photo = photo

    bg_label = Label(admin_window, image=admin_window.bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    def go_back():
        password_entry.delete(0, 'end')
        admin_window.destroy()         # закрываем личный кабинет
        win.deiconify()     # возвращаем в главное очко
        

    Button(admin_window, image=admin_window.photo,bg="#000213",bd = 0, command=go_back).place(x=30, y=30)