from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Canvas с фоном")

# Загружаем изображение для фона
bg_image = Image.open("res/BackGround.png")  # Укажите путь к своему изображению
bg_image = bg_image.resize((800, 600))  # Пример: изменяем размер изображения
bg_photo = ImageTk.PhotoImage(bg_image)



# Создаём Canvas и размещаем изображение как фон
canvas = Canvas(window, width=800, height=600)
canvas.pack()



# Устанавливаем изображение на Canvas
canvas.create_image(0, 0, image=bg_photo, anchor=NW)

# Можно рисовать другие элементы на Canvas
canvas.create_text(400, 300, text="Это Canvas с фоном!", font=("Arial", 16), fill="white")

# Изображение без фона на Canvas
image = Image.open("res/x.png")
tkimage = ImageTk.PhotoImage(image)
canvas.create_image(220, 250, image=tkimage)

window.mainloop()