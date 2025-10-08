from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        responses = requests.get(url)
        responses.raise_for_status()
        image_data = BytesIO(responses.content)
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"произошла ошибка: {e}")
        return None


def set_image():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img

def exit():
    window.destroy()



window = Tk()
window.title("Cats")
window.geometry("600x520")

label = Label()
label.pack()

# update_button = Button(text="обновить", command=set_image)
# update_button.pack()

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Файл", menu=filemenu)
filemenu.add_command(label="Загрузить фото", command=set_image)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=exit)

url = "https://cataas.com/cat"

set_image()

window.mainloop()
