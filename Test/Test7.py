from tkinter import *
import ctypes  # Работает только на Windows

root = Tk()
root.geometry("400x200")
root.title("Проверка Caps Lock")

# Создаём метку для Caps Lock предупреждения
caps_label = Label(root, text="", font=("Arial", 12), fg="red")
caps_label.pack(pady=10)

# Функция проверки Caps Lock
def check_caps_lock(event=None):
    # 0x14 — это код клавиши Caps Lock
    caps_on = ctypes.WinDLL("User32.dll").GetKeyState(0x14)
    if caps_on:
        caps_label.config(text="⚠️ CAPS LOCK ВКЛЮЧЕН")
    else:
        caps_label.config(text="")

# Поле ввода пароля
entry = Entry(root, show="*", font=("Arial", 14))
entry.pack(pady=20)
entry.bind("<KeyRelease>", check_caps_lock)  # Проверка при вводе

# Проверка при запуске
check_caps_lock()

root.mainloop()