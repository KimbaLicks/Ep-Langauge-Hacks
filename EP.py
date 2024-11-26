# Windows Version

import pytesseract
from PIL import ImageGrab
from deep_translator import GoogleTranslator
import pyautogui
import time
import os
import keyboard  # Import the keyboard library

# Set the TESSDATA_PREFIX environment variable
tessdata_dir = 'C:\\Program Files\\Tesseract-OCR'
os.environ['TESSDATA_PREFIX'] = tessdata_dir

# Check if the language file exists
if not os.path.isfile(os.path.join(tessdata_dir, 'tessdata', 'fra.traineddata')):
    raise FileNotFoundError("French language data file 'fra.traineddata' not found in TESSDATA_PREFIX directory.")

# Install tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

running = False  # Flag to control the main loop

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
    text = pytesseract.image_to_string(image, lang='fra')
    return text

def translate_text(text):
    translation = GoogleTranslator(source='fr', target='en').translate(text)
    return translation

def type_text(text):
    pyautogui.typewrite(text)

def process_text(translated_text):
    if "OUR ANSWER" in translated_text:
        print("Detected 'ANSWER' in the translated text. Skipping typing and waiting...")
        time.sleep(1.5)
        pyautogui.press('enter')
    else:
        print(f"Typing translated text: {translated_text}")
        type_text(translated_text)
        pyautogui.press('enter')

def main_loop(interval=10):
    global running
    while running:
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

def toggle_running():
    global running
    running = not running
    if running:
        print("Starting the main loop...")
        main_loop(interval=1)
    else:
        print("Stopping the main loop...")

# Set up the keyboard listener for the right Shift key
keyboard.add_hotkey('right shift', toggle_running)

if __name__ == "__main__":
    print("Press the right Shift key to start/stop the script.")
    keyboard.wait()  # Wait indefinitely for keyboard events
