from tkinter import *
from PIL import Image, ImageTk

window = Tk()

# Устанавливаем полноэкранный режим
window.attributes('-fullscreen', True)

# Получаем размеры экрана
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Создаем Frame, который будет занимать весь экран
frame = Frame(window, width=screen_width, height=screen_height)
frame.pack(fill=BOTH, expand=True)

# Загружаем изображение для фона
bg_image = Image.open("res/BackGround.png")  # Укажите путь к изображению
bg_image = bg_image.resize((screen_width, screen_height))  # Растягиваем под размер экрана
bg_photo = ImageTk.PhotoImage(bg_image)

# Размещаем фоновое изображение в Frame с помощью Label
bg_label = Label(frame, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Растягиваем картинку на весь Frame

# Создаем Canvas, но без фона, так как фон будет задаваться фоновым изображением
canvas = Canvas(frame, width=screen_width, height=screen_height, bd=0, highlightthickness=0)
canvas.place(relwidth=1, relheight=1)  # Растягиваем Canvas на весь Frame

# Добавляем кнопку на Canvas с изображением
button_image = PhotoImage(file="res/x.png")  # Укажите путь к изображению для кнопки

def on_button_click():
    print("Кнопка нажата!")

button = Button(canvas, image=button_image, command=on_button_click, bd=0, highlightthickness=0)
button.place(x=screen_width//2 - 100, y=screen_height//2 + 100)  # Позиционируем кнопку

# Запуск приложения
window.mainloop()