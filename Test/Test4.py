from tkinter import *
from PIL import Image, ImageTk

window = Tk()

# Устанавливаем полноэкранный режим
window.attributes('-fullscreen', True)

# Получаем размеры экрана
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Загружаем изображение для фона
bg_image = Image.open("res/BG.png")  # Укажите путь к изображению
bg_image = bg_image.resize((screen_width, screen_height))  # Растягиваем под размер экрана
bg_photo = ImageTk.PhotoImage(bg_image)

# Создаём Frame, который будет занимать весь экран
frame = Frame(window, width=screen_width, height=screen_height)
frame.pack(fill=BOTH, expand=True)

# Размещаем фоновое изображение в Frame с помощью Label
bg_label = Label(frame, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Растягиваем картинку на весь Frame

# Можно добавить другие элементы поверх фона
label = Label(frame, text="Полноэкранный режим с Frame", font=("Arial", 24), fg="white", bg="black")
label.pack(pady=50)

button = Button(frame, text="gyguy", command=window.destroy, bd=0, highlightthickness=0, relief=FLAT, fg="black", width=20, height=10)
button.place(x=screen_width//2 - 100, y=screen_height//2 + 100)  # Размещаем кнопку
button.config(cursor="hand2")


window.mainloop()