from PIL import Image
from RpiMotorLib import RpiMotorLib
import time

gpio_pins = (14,15,18)
direction = 20
step = 21
distance= 80
im = Image.open('hacksmith.jpg')
pix = im.load()

motor = RpiMotorLib.A4988Nema(direction, step, gpio_pins, "A4988")


def colorComparer(value):
    g = value[1]
    if g in range(245,265):
        print("Yellow")
        return "y"

    elif g in range(135,155):
        print("Orange")
        return "o"

    elif g in range(45,60):
        print("Blue")
        return "b"

    elif g in range(-5,15):
        print("Red")
        return 'r'


for y in range(59,-1,-1):
    for x in range(0, 40, 1):
        RGBValues = pix[x, y]
        motor.motor_go(False,"Full", 200, 0.0005, 0.5)
        time.sleep(1)
        color = colorComparer(RGBValues)
        if color == 'r':
            # open red servo stopper
            time.sleep(2)
        elif color == 'b':
            time.sleep(2)
            #open blue servo stopper
        elif color == 'o':
            time.sleep(2)
            # open yellow servo stopper
        elif color == 'y':
            #open yellow servo stopper
            time.sleep(2)
        if x == 39:
            motor.motor_go(True,"Full", 8000, 0.0001 , 0.5)
            time.sleep(1)




#20 51 116 is supposed to be blue
#229 146 8 is supposed to be orange
#252 255 0 is suppopsed to be yellow
#137 4 23 is supposed to be red