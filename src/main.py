import datetime
import time

import autoit
import cv2
import numpy as np
import pytesseract
from loguru import logger
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


# old
# SAVE_IMG = True
# RESET_TIME = 6.5
# CHANGE_TIME = 30
# prev_xp_value = None
# change_timestamp = datetime.datetime.now()
# FIRSTMOVE = True


# new
class GameHandler:
    def __init__(
        self,
    ):
        self.RESET_TIME = 9
        self.CHANGE_TIME = 30
        self.FIRSTMOVE = True
        self.SAVE_IMG = True
        self.prev_xp_value = None
        self.change_timestamp = datetime.datetime.now()
        self.start_time = 0
        self.started = False
        self.reset_time = datetime.datetime.now() + datetime.timedelta(
            minutes=self.RESET_TIME
        )


def main(attack: Inputs, level: Levels, game: GameHandler):
    game.start_time = 0
    game.FIRSTMOVE = True
    game.started = False
    game.reset_time = datetime.datetime.now() + datetime.timedelta(
        minutes=game.RESET_TIME
    )

    while True:
        now = datetime.datetime.now()

        xp_image = ImageGrab.grab(bbox=(80, 1010, 150, 1034))
        # convert the image to gray scale
        gray = cv2.cvtColor(np.array(xp_image), cv2.COLOR_BGR2GRAY)
        # threshold the gray image so that everything not white becomes black
        _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        if game.SAVE_IMG:
            cv2.imwrite("utils/imgs/xp_image.png", binary)

        current_xp_value = pytesseract.image_to_string(binary)

        if game.prev_xp_value != current_xp_value:
            game.prev_xp_value = current_xp_value
            game.change_timestamp = now

        # reset if time has passed the reset thrshold or the xp has not changed for the xp time limit
        if (
            now - game.change_timestamp > datetime.timedelta(seconds=game.CHANGE_TIME)
            or now >= game.reset_time
        ):
            if now >= game.reset_time:
                logger.info(f"Resetting after {game.RESET_TIME} time has passed, wow!")
            else:
                logger.info(
                    f"Resetting after {game.CHANGE_TIME} time has passed since receiving XP"
                )
            reset_after_time()
            game.started = False
            game.reset_time = now + datetime.timedelta(minutes=game.RESET_TIME + 0.4)
            game.change_timestamp = now
            game.prev_xp_value = None
            game.FIRSTMOVE = True

        # --------
        # claim button daily

        claim_image = ImageGrab.grab(bbox=(895, 735, 1010, 770))
        if game.SAVE_IMG:
            claim_image.save(
                "utils/imgs/claim_image.png"
            )  # saves the start_image as start_image.png
        claim_values = pytesseract.image_to_string(claim_image)
        if "Claim" in claim_values or "la" in claim_values:
            claim_image.save(
                "utils/imgs/claim_image_with_text.png"
            )  # saves the start_image as start_image.png
            time.sleep(1)
            autoit.mouse_click("left", 950, 750)

        start_image = ImageGrab.grab(bbox=(800, 850, 1100, 920))
        if game.SAVE_IMG:
            start_image.save(
                "utils/imgs/start_image.png"
            )  # saves the start_image as start_image.png
        start_values = pytesseract.image_to_string(start_image)

        retry_image = ImageGrab.grab(bbox=(600, 700, 690, 760))
        if game.SAVE_IMG:
            retry_image.save(
                "utils/imgs/retry_image.png"
            )  # saves the retry_image as retry_image.png
        retry_values = pytesseract.image_to_string(retry_image)

        if "Retry" in retry_values:
            logger.info(f"Retrying after death with retry value = {retry_values}")
            on_death()
            game.started = False
            game.reset_time = now + datetime.timedelta(minutes=game.RESET_TIME + 0.4)
            game.FIRSTMOVE = True
        elif "Start" in start_values and game.started == False:
            logger.info(f"Round started! with start value  = {start_values}")
            game.start_time = now
            game.FIRSTMOVE = True
            on_round_start(attack, level)
            game.started = True

        elif game.started == True:
            # logger.info("Regular gameplay loop initiated")
            regular_gameplay_loop(attack, game.FIRSTMOVE)
            game.FIRSTMOVE = False

        if game.started == True:
            round_time = (
                now - game.start_time if game.start_time else datetime.timedelta(0)
            )
            total_seconds = int(round_time.total_seconds())
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            current_xp_value_str = str(current_xp_value).strip()
            logger.info(
                f"XP:{current_xp_value_str:<12} time:{minutes:02d}:{seconds:02d}"
            )

        time.sleep(0.3)


if __name__ == "__main__":
    attack = Inputs(int(input("what attack, 1 = ability, 2 = sword")))
    level = Levels(int(input("what level, 1 = ancient, 2 = jungle")))
    game = GameHandler()

    main(attack, level, game)
