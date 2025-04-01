import time
import pytesseract
import mss
from googletrans import Translator
import tkinter as tk
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

translator = Translator()



root = tk.Tk()
root.title("Tradução")
root.geometry("800x300")
root.configure(bg="black", bd=0)
root.attributes("-topmost", True)
root.attributes("-transparentcolor", "black")

translation_label = tk.Label(root, text="", font=("Arial", 14), fg="white", bg="black", wraplength=500)
translation_label.pack(expand=True)

def update_translation(text):
    translation_label.config(text=text)

REGION = {'top': 715, 'left': 709, 'width': 500, 'height': 200}

def capture_and_translate():
    with mss.mss() as sct:
        while True:
            screenshot = sct.grab(REGION)

            img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

            text = pytesseract.image_to_string(img)
            text = text.replace("|", "i")
            if text.strip():
                translated_text = translator.translate(text, dest='pt').text

                update_translation(f"{translated_text}")


            time.sleep(1)


if __name__ == "__main__":
    import threading

    thread = threading.Thread(target=capture_and_translate)
    thread.daemon = True
    thread.start()

    root.mainloop()