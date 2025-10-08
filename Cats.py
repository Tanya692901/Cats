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
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"произошла ошибка: {e}")
        return None


def set_image():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img

window = Tk()
window.title("Cats")
window.geometry("600x480")

label = Label()
label.pack()

update_button = Button(text="обновить", command=set_image)
update_button.pack()

url = "https://cataas.com/cat"

set_image()

window.mainloop()
