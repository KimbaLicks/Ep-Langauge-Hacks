import pytesseract
from PIL import ImageGrab
from googletrans import Translator
import pyautogui
import time

# Path to your tesseract executable (Homebrew installs it in /opt/homebrew/bin/tesseract by default)
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'


def get_centered_bbox(width, height):
    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Calculate bounding box dimensions
    left = (screen_width - width) // 2
    top = (screen_height - height) // 2 + 100
    right = left + width
    bottom = top + height

    return (left, top, right, bottom)


def capture_screen(width=400, height=100):
    # Calculate bounding box for centered capture
    bbox = get_centered_bbox(width, height)
    screen = ImageGrab.grab(bbox=bbox)
    # screen.show()
    return screen


def ocr_to_text(image):
    # Convert image to text
    text = pytesseract.image_to_string(image, lang='fra')  # Specify language as French
    return text

def translate_text(text):
    translator = Translator()
    translation = translator.translate(text, src='fr', dest='en')
    return translation.text

def type_text(text):
    # Type the translated text
    pyautogui.typewrite(text)

if __name__ == "__main__":
    time.sleep(2)  # Time to switch to the screen you want to capture
    image = capture_screen()
    french_text = ocr_to_text(image)
    print(f"Detected French Text: {french_text}")  # For debugging
    translated_text = translate_text(french_text)
    print(f"Translated Text: {translated_text}")  # For debugging
    type_text(translated_text)
