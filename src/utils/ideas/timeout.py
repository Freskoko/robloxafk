import time

import numpy as np
import pyautogui
import pytesseract
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\Henrik\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)

import time
from datetime import datetime

import pytesseract
from PIL import ImageGrab

prev_damage_value = None
change_timestamp = datetime.now()

while True:
    damage_image = ImageGrab.grab(bbox=(80, 1010, 145, 1030))

    current_damage_value = pytesseract.image_to_string(damage_image)
    print(current_damage_value)

    if prev_damage_value != current_damage_value:
        prev_damage_value = current_damage_value
        change_timestamp = datetime.now()

    now = datetime.now()
    elapsed_time = now - change_timestamp
    if elapsed_time.total_seconds() > 30:
        print("Damage value has not changed for 30 seconds, breaking...")
        break

    time.sleep(1)  # Put the program to sleep for 1 second to avoid high CPU usage
