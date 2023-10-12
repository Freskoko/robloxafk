import time
import autoit
import random

time.sleep(1)

def press_and_release(key: str, hold_time: float):
    autoit.send("{%s down}" % key)
    time.sleep(hold_time)
    autoit.send("{%s up}" % key)
    time.sleep(random.uniform(0.1, 0.3))  # Random delay before the next action

while True:
    time.sleep(random.uniform(0.9, 1.1))  # Random delay before starting the loop

    press_and_release("r", 0.25)
    time.sleep(random.uniform(4.5, 5.5))

    press_and_release("SPACE", 0.2)
    time.sleep(random.uniform(0.2, 0.25))

    press_and_release("SPACE", 0.1)
    time.sleep(random.uniform(0.43, 0.53))

    autoit.send("f down")
    time.sleep(random.uniform(64, 66))
    autoit.send("f up")
    
    time.sleep(random.uniform(0.09, 0.11))