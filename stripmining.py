import pyautogui as ag
import datetime,time
import sys


print('Press Ctrl-C to quit.')

print("Forward Mining[F] or Side Mining[S]")
y = input()
if y.upper() == "F":
    x = input("How many blocks?")
    mining = False
    if x.upper() == "R":
        mining = True
    try:
        print("Starting to mine {} in 3 seconds, set up the game!".format(x))
        time.sleep(3)
        while mining == True:
            ag.dragRel(1000, 1, 1.3)
            ag.keyDown("shift")
            ag.keyDown("W")
            time.sleep(0.5)
            ag.keyUp("W")
            ag.keyUp("shift")
        if mining == False:
            for i in range(int(x)):

                ag.dragRel(1000, 1, 1.3)
                ag.keyDown("shift")
                ag.keyDown("W")
                time.sleep(0.5)
                ag.keyUp("W")
                ag.keyUp("shift")


        print("finished mining!")
    except KeyboardInterrupt:
        print("Exited correctly")

elif y.upper() == "S":
    b = input("How many blocks?")

    def left_or_right():
        direc = (input("Left[L] or Right[R]?")).upper()
        if direc == "R" or direc == "L":
            return direc
        else:
            left_or_right()

    a = left_or_right()

    mining = False
    if b.upper() == "R":
        mining = True
    try:
        print("Starting to mine {} in 3 seconds, set up the game!".format(b))
        time.sleep(3)
        while mining == True:
            ag.dragRel(1, 1, 3)
            if a == "L":
                ag.keyDown("A")
            else:
                ag.keyDown("D")
            time.sleep(0.5)
            if a == "L":
                ag.keyUp("A")
            else:
                ag.keyUp("D")
        if mining == False:
            for i in range(int(b)):
                ag.dragRel(1, 1, 3)
                if a == "L" : ag.keyDown("A")
                elif a == "R": ag.keyDown("D")
                time.sleep(0.5)
                if a == "L":
                    ag.keyUp("A")
                elif a == "R":
                    ag.keyUp("D")

        print("finished mining!")
    except KeyboardInterrupt:
        print("Exited correctly")




