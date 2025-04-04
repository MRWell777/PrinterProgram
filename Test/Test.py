from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry("1100x500")
root['bg'] = 'red'                                          # +++

img = Image.open("res/x.png")
earrth = ImageTk.PhotoImage(img)
earth = Label(root, image=earrth)
earth.grid(row=0, column=0)

img2 = Image.open("res/x.png")
earrth2 = ImageTk.PhotoImage(img2)
earth2 = Label(root, image=earrth2)
earth2.config(bg="grey")                                    # +++
earth2.grid(row=0, column=1)

canvas = Canvas(root, width=600, height=500, 
     highlightthickness=0)                        # +++
canvas.grid(row=0, column=2, 
    padx=10, pady=10, ipadx=0, ipady=0,)     
image = Image.open("res/x.png")
tkimage = ImageTk.PhotoImage(image)
canvas_obj = canvas.create_image(220, 250, image=tkimage)

root.mainloop()