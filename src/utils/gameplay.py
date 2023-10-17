import time
from enum import Enum

import autoit


class Inputs(Enum):
    ABILITY = 1
    SWORD = 2


class Levels(Enum):
    ANCIENT = 1
    JUNGLE = 2


def hold_key(key, hold_time):
    start = time.time()
    while time.time() - start < hold_time:
        autoit.send(key)
        # time.sleep(0.01)


def on_round_start(attack, level):
    hold_key("s",3.7)

    if level == Levels.JUNGLE:
        hold_key("a", 3.9)

    autoit.mouse_click("left", 940, 886)
    time.sleep(1.2)
    if attack == Inputs.ABILITY:
        autoit.send("2")
    if attack == Inputs.SWORD:
        # autoit.send("1")
        pass  # clicks one by itself

    time.sleep(0.3)
    autoit.mouse_wheel("up", 200)  
    time.sleep(0.2)
    autoit.mouse_wheel("down", 200)  
    time.sleep(0.1)

    # Get the current mouse position
    current_pos = autoit.mouse_get_pos()

    # Move the mouse to the new position
    autoit.mouse_move(current_pos[0], current_pos[1] + 20, speed=10)

    return


def on_death():
    autoit.mouse_click("left", 683, 741)
    print("hi back retry")

FIRST_MOVE = True
def regular_gameplay_loop(attack, FIRST_MOVE):

    if attack == Inputs.ABILITY:

        if FIRST_MOVE:
            autoit.send("c")
            time.sleep(7)
            autoit.send("v")
            FIRST_MOVE = False

        autoit.send("c")
        # time.sleep(0.1)

        autoit.send("v")
        # time.sleep(0.1)
    
        autoit.send("r")
        # time.sleep(0.1)

        autoit.send("f")
        # time.sleep(0.1)

        autoit.send("g")
        # time.sleep(0.1)

        autoit.send("e")
        autoit.send("z")

        # autoit.send("g") #dont have it yet
        # time.sleep(0.1)


    if attack == Inputs.SWORD:
        autoit.mouse_click("left")
        autoit.send("{SPACE}")
        autoit.mouse_click("left")
        autoit.send("{SPACE}")

    time.sleep(0.5)
    # hold_key("s",0.1)
    # hold_key("w",0.4)


def reset_after_time():
    time.sleep(1)
    autoit.mouse_click("left", 280, 40)  # leave dungeons
    time.sleep(1)
    autoit.mouse_click("left", 850, 700)  # proceed
    time.sleep(30)
    autoit.mouse_click("left", 1000, 600)  # PLAY
    time.sleep(1)
    autoit.mouse_click("left", 1710, 900)  # PLAY again
    time.sleep(1)
    autoit.mouse_click("left", 600, 400)  # CREATE LOBBY
    time.sleep(1)
    autoit.mouse_click("left", 1400, 400)  # JUNGLE
    time.sleep(1)
    autoit.mouse_click("left", 560, 740)
    time.sleep(1)

    autoit.mouse_wheel("down", 300)  # Scrolls down one "click" of the mouse wheel.

    time.sleep(2)
    autoit.mouse_click("left", 560, 740)
    time.sleep(1)
    autoit.mouse_click("left", 1350, 800)
    time.sleep(1)
    autoit.mouse_click("left", 1360, 700)

    return

# implemented attack for angel
# if attack == Inputs.ABILITY:
#     autoit.send("{SPACE}")
#     time.sleep(0.1)
#     hold_key("f", 3)
#     autoit.send("r")
#     time.sleep(0.1)
#     autoit.send("{SPACE}")

#for dragon