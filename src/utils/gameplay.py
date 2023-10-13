from enum import Enum
import autoit
import time

class Inputs(Enum):
    ABILITY=1
    SWORD=2

class Levels(Enum):
    ANCIENT=1
    JUNGLE=2

def hold_key(key, hold_time):

    start = time.time()
    while time.time() - start < hold_time:
        autoit.send(key)
        # time.sleep(0.01)

def on_round_start(attack,level):


    hold_key("s", 4)

    if level == Levels.JUNGLE:
        hold_key("a", 4)
    
    autoit.mouse_click("left", 940, 886)
    time.sleep(1.2)
    if attack == Inputs.ABILITY:
        autoit.send("2")
    if attack == Inputs.SWORD:
        # autoit.send("1")
        pass #clicks one by itself

    return

def on_death():
    autoit.mouse_click("left", 683, 741)
    print("hi back retry")

def regular_gameplay_loop(attack):

    if attack == Inputs.ABILITY:
        autoit.send("{SPACE}")
        time.sleep(0.1)
        hold_key("f", 3)
        autoit.send("r")

    if attack == Inputs.SWORD:
        autoit.mouse_click("left")
        autoit.send("{SPACE}")
        autoit.mouse_click("left")

    time.sleep(0.5)
    hold_key("w",0.5)
    hold_key("s",0.5)

def reset_after_stuck():
    #280, 40 leave dungeoms

    # time sleep

    #350, 700 proceed
    
    # time sleep

    #1000, 600 PLAY

    # 1800,900 PLAY

    # 600, 400 CREATE LOBBY

    #1400,400 JUNGLE

    # 560, 740 , THEN SCROLL DOWN AS MUCH AS POSSIBLE

    # 1350, 800

    #1360, 700

    return