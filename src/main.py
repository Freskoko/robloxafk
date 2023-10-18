import datetime
import time

import pytesseract
from loguru import logger
from PIL import ImageGrab

from utils.gameplay import (Inputs, Levels, on_death, on_round_start,
                            regular_gameplay_loop, reset_after_time)

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\Henrik\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)

RESET_TIME = 1000000000
CHANGE_TIME = 30
prev_xp_value = None
change_timestamp = datetime.datetime.now()

FIRSTMOVE = True


def main(attack, level):
    global prev_xp_value
    global change_timestamp
    global start_time
    start_time = 0
    FIRSTMOVE = True
    started = False
    reset_time = datetime.datetime.now() + datetime.timedelta(minutes=RESET_TIME)

    while True:
        now = datetime.datetime.now()

        xp_image = ImageGrab.grab(bbox=(80, 1010, 145, 1030))
        current_xp_value = pytesseract.image_to_string(xp_image)

        if prev_xp_value != current_xp_value:
            prev_xp_value = current_xp_value
            change_timestamp = now

        # RESET AFTER MINUTES -> Not needed since we restart if no xp change, but still nice to have
        if (
            now - change_timestamp > datetime.timedelta(seconds=CHANGE_TIME)
            or now >= reset_time
        ):
            if now >= reset_time:
                logger.info(f"Resetting after {RESET_TIME} time has passed, wow!")
            else:
                logger.info(
                    f"Resetting after {CHANGE_TIME} time has passed since receiving XP"
                )
            reset_after_time()
            started = False
            reset_time = now + datetime.timedelta(minutes=RESET_TIME + 0.4)
            change_timestamp = now
            prev_xp_value = None
            FIRSTMOVE = True

        start_image = ImageGrab.grab(bbox=(800, 850, 1100, 920))
        start_values = pytesseract.image_to_string(start_image)

        retry_image = ImageGrab.grab(bbox=(600, 700, 690, 760))
        retry_values = pytesseract.image_to_string(retry_image)

        if "Retry" in retry_values:
            logger.info(f"Retrying after death with retry value = {retry_values}")
            on_death()
            started = False
            reset_time = now + datetime.timedelta(minutes=RESET_TIME + 0.4)
            FIRSTMOVE = True
        elif "Start" in start_values and started == False:
            logger.info(f"Round started! with start value  = {start_values}")
            start_time = now
            FIRSTMOVE = True
            start_time = now
            on_round_start(attack, level)
            started = True

        elif started == True:
            # logger.info("Regular gameplay loop initiated")
            regular_gameplay_loop(attack, FIRSTMOVE)
            FIRSTMOVE = False

        if started == True:
            round_time = now - start_time if start_time else 0
            logger.info(f"XP = {current_xp_value} time = {round_time}")

        time.sleep(0.3)


if __name__ == "__main__":
    attack = Inputs(int(input("what attack, 1 = ability, 2 = sword")))
    level = Levels(int(input("what level, 1 = ancient, 2 = jungle")))

    main(attack, level)
