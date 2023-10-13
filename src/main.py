import datetime
import threading
import time

import pytesseract
from PIL import ImageGrab

from utils.gameplay import (
    Inputs,
    Levels,
    on_death,
    on_round_start,
    regular_gameplay_loop,
    reset_after_time,
)

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\Henrik\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)

RESET_TIME = 2


def main(attack, level):
    started = False
    reset_time = datetime.datetime.now() + datetime.timedelta(minutes=RESET_TIME)
    while True:
        now = datetime.datetime.now()
        if now >= reset_time:
            reset_after_time()
            reset_time = now + datetime.timedffffffffffffffffffffffffffffffffffffffrelta(minutes=RESET_TIME + 0.4)

        start_image = ImageGrab.grab(bbox=(800, 850, 1100, 920))
        start_values = pytesseract.image_to_string(start_image)

        retry_image = ImageGrab.grab(bbox=(600, 700, 690, 760))
        retry_values = pytesseract.image_to_string(retry_image)

        print(start_values)
        print(retry_values)

        if "Retry" in retry_values:
            on_death()
            started = False
        elif "Start" in start_values:
            on_round_start(attack, level)
            started = True
        elif started == True:
            regular_gameplay_loop(attack)

        time.sleep(1)
        # start a timer, after 5 minutes, call the reset


if __name__ == "__main__":
    attack = Inputs(int(input("what attack, 1 = ability, 2 = sword")))
    level = Levels(int(input("what level, 1 = ancient, 2 = jungle")))

    main(attack, level)
