from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

window = Tk()
window.title("Cats")
window.geometry("600x480")

label = Label()
label.pack()

Url = "https://cataas.com/cat"
img = load.Image(Url)

if img:
    label.configure(image=img)
    label.image = img

window.mainloop()




