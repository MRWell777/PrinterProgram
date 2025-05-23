from tkinter import *
from OpenMenu import open_quest_user

if __name__ == "__main__":
    root = Tk()
    Button(root, text="Открыть анкету", command=lambda: open_quest_user()).pack(pady=50)
    root.mainloop()