from http.client import responses
from tkinter import *
from urllib import response
from PIL import Image, ImageTk
import requests
from io import BytesIO

from urllib3.util import url


def load_image():
    try:
        responses = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(responses.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"произошла ошибка: {e}")
        return None





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




