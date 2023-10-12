import time
import pytesseract
from PIL import ImageGrab
from utils.gameplay import Levels, on_death, on_round_start, regular_gameplay_loop
from utils.gameplay import Inputs

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Henrik\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def main(attack,level):
    started = False
    while(True):
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
            on_round_start(attack,level)
            started = True
        elif started == True:
            regular_gameplay_loop(attack)

        time.sleep(1)

if __name__ == "__main__":
    attack = Inputs(int(input("what attack, 1 = ability, 2 = sword")))
    level = Levels(int(input("what level, 1 = ancient, 2 = jungle")))

    main(attack,level)
