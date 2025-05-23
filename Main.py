from tkinter import *
from window import Window ## У меня пиздит, что такой библиотеки не знает, может это с ТКинтера библиотека?

def main():
    Window
    # Инициализация приложения
    app = Window()
    app.mainloop()

if __name__ == "__main__":
    main()
