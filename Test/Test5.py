from tkinter import *
from PIL import Image, ImageTk

window = Tk()

# Устанавливаем полноэкранный режим
window.attributes('-fullscreen', True)

# Получаем размеры экрана
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Загружаем изображение для фона
bg_image = Image.open("res/BackGround.png")  # Укажите путь к изображению
bg_image = bg_image.resize((screen_width, screen_height))  # Растягиваем под размер экрана
bg_photo = ImageTk.PhotoImage(bg_image)

# Создаём Frame, который будет занимать весь экран
frame = Frame(window, width=screen_width, height=screen_height)
frame.pack(fill=BOTH, expand=True)

# Размещаем фоновое изображение в Frame с помощью Label
bg_label = Label(frame, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Растягиваем картинку на весь Frame

# Создаём Canvas, который будет прозрачным
canvas = Canvas(window, width=screen_width, height=screen_height, bd=0, highlightthickness=0)
canvas.place(relwidth=1, relheight=1)  # Растягиваем Canvas на весь Frame

#canvas.create_image(0, 0, image=bg_photo, anchor=NW)

# Можно добавить элементы на Canvas (например, текст или изображения)
canvas.create_text(screen_width // 2, screen_height // 2, text="Canvas с прозрачным фоном", font=("Arial", 24), fill="white")

# Дополнительно добавим картинку на Canvas (например, для логотипа)
overlay_image = Image.open("res/x.png")  # Укажите путь к дополнительной картинке
overlay_image = overlay_image.resize((200, 200))  # Изменяем размер картинки
overlay_photo = ImageTk.PhotoImage(overlay_image)

# Добавляем картинку на Canvas
canvas.create_image(screen_width//2, screen_height//2 + 100, image=overlay_photo)

button = Button(frame, text="   ", command=window.destroy, bd=0, highlightthickness=0, relief=FLAT, bg=frame.cget("bg"), fg="black", width=20, height=10)
button.place(x=screen_width//2 - 100, y=screen_height//2 + 100)  # Размещаем кнопку
button.config(cursor="hand2")

window.mainloop()