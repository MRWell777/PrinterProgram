

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Навигация")
        self.geometry("400x300")

        self.frames = {}
        self.history = []

        for F in (HomePage, PageOne, PageTwo):
            frame = F(self)
            self.frames[F.__name__] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("HomePage", remember=False)

    def show_frame(self, name, remember=True):
        frame = self.frames[name]
        frame.tkraise()
        if remember:
            if not self.history or self.history[-1] != name:
                self.history.append(name)

    def go_back(self):
        if len(self.history) > 1:
            self.history.pop()
            prev = self.history[-1]
            self.show_frame(prev, remember=False)

    def go_home(self):
        self.history.clear()
        self.show_frame("HomePage", remember=False)

# Страницы

class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="🏠 Главная", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="На страницу 1", command=lambda: master.show_frame("PageOne")).pack(pady=5)

class PageOne(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="📄 Страница 1", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="На страницу 2", command=lambda: master.show_frame("PageTwo")).pack(pady=5)
        #tk.Button(self, text="Назад", command=master.go_back).pack(pady=5)
        tk.Button(self, text="На главную", command=master.go_home).pack(pady=5)

class PageTwo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="📄 Страница 2", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="Назад", command=master.go_back).pack(pady=5)
        tk.Button(self, text="На главную", command=master.go_home).pack(pady=5)

app = App()
app.mainloop()