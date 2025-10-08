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


def open_new_window():
    tag = tag_entry.get()
    url_tag = f"https://cataas.com/cat/{tag}"if tag else "https://cataas.com/cat"
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img

def exit():
    window.destroy()



window = Tk()
window.title("Cats")
window.geometry("600x520")
tag_entry = Entry()
tag_entry.pack()

load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()



# update_button = Button(text="обновить", command=set_image)
# update_button.pack()

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Файл", menu=filemenu)
filemenu.add_command(label="Загрузить фото", command=open_new_window)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=exit)

url = "https://cataas.com/cat"


window.mainloop()
