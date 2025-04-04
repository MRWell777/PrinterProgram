import customtkinter as ctk
from PIL import Image, ImageTk

# Создаем главное окно
window = ctk.CTk()



# Устанавливаем полноэкранный режим
window.attributes('-fullscreen', True)

# Получаем размеры экрана
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Загружаем изображение для фона
bg_image = Image.open("res/BackGround.png")  # Укажите путь к изображению
bg_image = bg_image.resize((screen_width, screen_height))  # Изменяем размер под экран
bg_photo = ImageTk.PhotoImage(bg_image)

# Создаем Canvas с размерами экрана
canvas = ctk.CTkCanvas(window, width=screen_width, height=screen_height,bd=0, highlightthickness=0)
canvas.pack()

# Устанавливаем изображение на Canvas
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Можно рисовать другие элементы поверх фона
canvas.create_text(screen_width // 2, screen_height // 2, text="Полноэкранный режим", font=("Arial", 24), fill="white")

# Загрузка дополнительного изображения (например, кнопки)
image = Image.open("res/x.png")  # Путь к изображению
tkimage = ImageTk.PhotoImage(image)
canvas.create_image(220, 250, image=tkimage)

# Запуск главного цикла
window.mainloop()