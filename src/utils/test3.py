import time
import autoit

def hold_key(key, hold_time):
    start = time.time()
    while time.time() - start < hold_time:
        autoit.send(key)
        # time.sleep(0.01)

def click_move(x,y):
    autoit.mouse_click("right", x, y)
    time.sleep(0.1)
    autoit.mouse_click("right", x, y)
    time.sleep(1)

def attack(ability,x,y):
    time.sleep(0.1)
    autoit.mouse_click("left", x, y)
    time.sleep(0.1)
    autoit.send(ability)
    time.sleep(1)

time.sleep(1)
autoit.mouse_wheel("up", 200)  
time.sleep(0.2)
autoit.mouse_wheel("down", 200)  
time.sleep(0.1)

current_pos = autoit.mouse_get_pos()

# Move the mouse to the new position
# autoit.mouse_move(current_pos[0], current_pos[1] + 30, speed=10)

autoit.mouse_click_drag(button="right",
                        x1 = current_pos[0],
                        y1 =current_pos[1],
                        x2 = current_pos[0],
                        y2 =current_pos[1]+30,
                        )


# time.sleep(1)
# hold_key("a",2)

time.sleep(2)
hold_key("w",10)

time.sleep(1)
hold_key("a",4)

time.sleep(1)
hold_key("w",2)
#now im in the corner, use mouse from now on

#------------------
#click start
time.sleep(1)
autoit.mouse_click("left", 940, 886)
time.sleep(3)

#move past gate
for i in range(2):
    click_move(1050, 1040)
    time.sleep(2.5)

#move a little further up
# 1050,975
# click_move()

click_move(1075,800)

#go to ability
autoit.send("2")

#attack enemy with R
attack("r",900,900)

click_move(650,710)

time.sleep(10)
attack("r",900,850)





