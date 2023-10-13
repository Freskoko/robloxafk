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
    hold_key("s", 4)

    if level == Levels.JUNGLE:
        hold_key("a", 4)

    autoit.mouse_click("left", 940, 886)
    time.sleep(1.2)
    if attack == Inputs.ABILITY:
        autoit.send("2")
    if attack == Inputs.SWORD:
        # autoit.send("1")
        pass  # clicks one by itself

    return


def on_death():
    autoit.mouse_click("left", 683, 741)
    print("hi back retry")


def regular_gameplay_loop(attack):
    # implemented for angel
    if attack == Inputs.ABILITY:
        autoit.send("{SPACE}")
        time.sleep(0.1)
        hold_key("f", 3)
        autoit.send("r")
        time.sleep(0.1)
        autoit.send("{SPACE}")

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
    time.sleep(15)
    autoit.mouse_click("left", 1000, 600)  # PLAY
    time.sleep(1)
    autoit.mouse_click("left", 1800, 900)  # PLAY again
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
