from PIL import Image
from RpiMotorLib import RpiMotorLib, rpiservolib
import time

gpio_pins = (14,15,18)
direction = 20
step = 21
distance= 80
im = Image.open('hacksmith.jpg')
pix = im.load()

servo  = rpiservolib.SG90servo("servoone", 50, 2, 12)
servo2  = rpiservolib.SG90servo("servotwo", 50, 2, 12)
servo3  = rpiservolib.SG90servo("servothree", 50, 2, 12)
servo4  = rpiservolib.SG90servo("servofour", 50, 2, 12)
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

def ServoMover(color):
    if color =='r':
        servo.servo_move(7, 11, 1, False, .01)
        time.sleep(2)
    if color =='y':
        servo.servo_move(7, 11, 1, False, .01)
        time.sleep(2)
    if color == 'o':
        servo.servo_move(7, 11, 1, False, .01)
        time.sleep(2)
    if color == 'b':
        servo.servo_move(7, 11, 1, False, .01)
        time.sleep(2)





for y in range(59,-1,-1):
    for x in range(0, 40, 1):
        RGBValues = pix[x, y]
        motor.motor_go(False,"Full", 200, 0.0005, 0.5)
        time.sleep(1)
        color = colorComparer(RGBValues)
        ServoMover(color)



#20 51 116 is supposed to be blue
#229 146 8 is supposed to be orange
#252 255 0 is suppopsed to be yellow
#137 4 23 is supposed to be red