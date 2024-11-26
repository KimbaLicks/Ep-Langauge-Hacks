# This is the mac version

import pytesseract
from PIL import ImageGrab
from googletrans import Translator
import pyautogui
import time

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

import pytesseract
from PIL import ImageGrab
from googletrans import Translator
import pyautogui
import time

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'


def get_centered_bbox(width, height):
    screen_width, screen_height = pyautogui.size()

    left = (screen_width - width) // 2 - 200
    top = (screen_height - height) // 2 + 150
    right = left + width + 400
    bottom = top + height + 200

    return (left, top, right, bottom)


def capture_screen(width=400, height=100):
    bbox = get_centered_bbox(width, height)
    screen = ImageGrab.grab(bbox=bbox)
    return screen



def ocr_to_text(image):
    # Convert image to text
    text = pytesseract.image_to_string(image, lang='fra')
    return text

def translate_text(text):
    translator = Translator()
    translation = translator.translate(text, src='fr', dest='en')
    return translation.text

def type_text(text):
    pyautogui.typewrite(text)

def process_text(translated_text):
    if "OUR ANSWER" in translated_text:
        print("Detected 'ANSWER' in the translated text. Skipping typing and waiting...")
        time.sleep(1.5)
        pyautogui.press('enter')
    else:
        print("Typing translated text: {translated_text}")
        type_text(translated_text)
        pyautogui.press('enter')

def main_loop(interval=10):
    while True:
        print("Starting new capture...")
        image = capture_screen(width=200, height=200)
        french_text = ocr_to_text(image)
        print(f"Detected French Text: {french_text}")
        if french_text.strip():
            translated_text = translate_text(french_text)
            print(f"Translated Text: {translated_text}")
            process_text(translated_text)
        else:
            print("No text detected.")
        print(f"Waiting for {interval} seconds...")
        time.sleep(interval)

if __name__ == "__main__":
    time.sleep(5)
    main_loop(interval=1)
