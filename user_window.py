from tkinter import Button, Toplevel, Label
from PIL import Image, ImageTk


def open_user_window(win,password_entry):

    win.withdraw()
    
    user_window = Toplevel(win)
    user_window.title("Личный кабинет пользователя")
    user_window.geometry("400x300")
    user_window.attributes('-fullscreen', True)

    image = Image.open("res/exit.png").convert("RGBA")  
    photo = ImageTk.PhotoImage(image)
    
    screen_width = user_window.winfo_screenwidth()
    screen_height = user_window.winfo_screenheight()

    bg_image = Image.open("res/BackGroundUser.png")  # Укажите путь к изображению
    bg_image = bg_image.resize((screen_width, screen_height))  # Изменяем размер под экран
    bg_photo = ImageTk.PhotoImage(bg_image)

    user_window.bg_photo = bg_photo #сохранение данных
    user_window.photo = photo

    bg_label = Label(user_window, image=user_window.bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    
    

    def go_back():
        password_entry.delete(0, 'end')
        user_window.destroy()         # закрываем личный кабинет
        win.deiconify()     # возвращаем главное окно

    Button(user_window,image=user_window.photo,bg="#000213",bd = 0, command=go_back).place(x=30, y=30)
    
        
        

    

    