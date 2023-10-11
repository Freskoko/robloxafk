import time
import pytesseract
import autoit
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Henrik\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def hold_key(key, hold_time):
    """
    FIX THIS!!
    """
    start = time.time()
    while time.time() - start < hold_time:
        autoit.send(key)
        time.sleep(0.01)

def on_round_start():
    hold_key("s", 4)
    hold_key("a", 4)
    autoit.send("2")
    autoit.mouse_click("left", 940, 886)
    return

def on_death():
    autoit.mouse_click("left", 683, 741)
    print("hi back retry")
    return 

def regular_gameplay_loop():
    autoit.send("f")
    autoit.send("r")
    autoit.send("{SPACE}")

def main():
    while(True):
        start_image = ImageGrab.grab(bbox=(800, 850, 1100, 920))
        start_values = pytesseract.image_to_string(start_image)

        retry_image = ImageGrab.grab(bbox=(600, 700, 690, 760))
        retry_values = pytesseract.image_to_string(retry_image)

        print(start_values)
        print(retry_values)
        if "Retry" in retry_values:
            on_death()
        elif "Start" in start_values:
            on_round_start()
        else:
            regular_gameplay_loop()

        time.sleep(1)

if __name__ == "__main__":
    main()
