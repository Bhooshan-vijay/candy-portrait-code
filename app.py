# This library gives the color value of each pixel
from _typeshed import StrOrBytesPath
from PIL import Image

# This library gives control to the stepper motor and the servo motors
from RpiMotorLib import RpiMotorLib, rpiservolib

# This library helps in giving delays to stop the code if needed
import time

#this library helps in controlling the pins of the raspberry pi
import RPi.GPIO as GPIO

#the sys module provides information about constants, functions and methods etc. here we are using a function of this library to stop the code execution if a certain value is true
import sys

GPIO.setmode(GPIO.BOARD)         #Set GPIO pin numbering

GPIO.setup(12, GPIO.IN, pull_down=GPIO.PUD_DOWN)  #Enables input pin  and sets an internal pull down resistor


gpio_pins = (14,15,18)  #this variable declares the pins that will control the stepper motor 1
direction = 20          # this pin controls the direction of motor 1
step = 21               # this pin controls the step of motor 1

gpio_pins2 = (9,10,11)  #this variable declares the pins that will control the stepper motor 2
direction2 = 12         # this pin controls the direction of motor 2
step2 = 13              # this pin controls the step of motor 2

image = Image.open('hacksmith.jpg')   # this variable will open the image and store
pixel = image.load()                  # this variable loads the image and stores the value of it

servo  = rpiservolib.SG90servo("servoone", 50, 2, 12)
servo2  = rpiservolib.SG90servo("servotwo", 50, 2, 12)
servo3  = rpiservolib.SG90servo("servothree", 50, 2, 12)
servo4  = rpiservolib.SG90servo("servofour", 50, 2, 12)

motor = RpiMotorLib.A4988Nema(direction, step, gpio_pins, "A4988")
motor1 = RpiMotorLib.A4988Nema(direction2, step2, gpio_pins2, "A4988")

#This function will compare the color values of each pixel and returns a value what the color can be 
def colorComparer(value):

    g = value[1]   # this function will store the second value of the value given which are the values of color green

    if g in range(245,265):
        print("Yellow")
        return "yellow"

    elif g in range(135,155):
        print("Orange")
        return "orange"

    elif g in range(45,60):
        print("Blue")
        return "blue"

    elif g in range(-5,15):
        print("Red")
        return 'red'

#This function will move the servos according to the color value of the pixel
def ServoMover(color):

        if color =='red':
            servo.servo_move(7, 11, 1, False, .01)    # if the color is red then the servo will move ........ this is left
            time.sleep(2)

        if color =='yellow':
            servo.servo_move(7, 11, 1, False, .01)
            time.sleep(2)

        if color == 'orange':
            servo.servo_move(7, 11, 1, False, .01)
            time.sleep(2)

        if color == 'blue':
            servo.servo_move(7, 11, 1, False, .01)
            time.sleep(2)

for y in range(59,-1,-1):
 
    for x in range(0, 40, 1):

        RGBValues = pixel[x, y]                                  # this variable will store the rgb color value of the pixel value given to it

        input = GPIO.input(12)                                   # this variable store the values that are coming to the input pin
        
        steps = 1

        for acceleration in range(0.0165, 0.0004,-2):
            
            motor.motor_go(False,"Full", 1, acceleration, 0)           # this function will make the motor 1 run clockwise with full steps and take 1 steps with a delay of value acceleration between each step 
            motor1.motor_go(True,"FUll", 1, acceleration, 0)           # this function will make the motor 2 run anti - clockwise with full steps and take 1 steps with a  delay of value acceleration between each step 
            steps += 1

            if steps == 80:
                motor.motor_go(False,"Full", 40, 0.0005, 0)
                motor1.motor_go(True, "Full", 40, 0.0005, 0)

                for deceleration in range(0.0005, 0.0166, 2):
                    motor.motor_go(False, "Full", 1, deceleration, 0)
                    motor1.motor_go(True, "Full", 1, deceleration, 0)
        
        time.sleep(1)                                            # this function will stop the code for 1 second

        color = colorComparer(RGBValues)                         # the variable will store the values sent back by the function created

        if x == 39:
            # if this if statement is true then the the motors will go back to the initial position
            for acceleration in range(0.0165, 0.0004,-1):
            
                motor.motor_go(False,"Full", 1, acceleration, 0)           # this function will make the motor 1 run clockwise with full steps and take 1 steps with a delay of value acceleration between each step 
                motor1.motor_go(True,"FUll", 1, acceleration, 0)           # this function will make the motor 2 run anti - clockwise with full steps and take 1 steps with a  delay of value acceleration between each step 
                steps += 1

                if steps == 80:
                    motor.motor_go(False,"Full", 7680, 0.0005, 0)
                    motor1.motor_go(True, "Full",7680, 0.0005, 0)

                    for deceleration in range(0.0005, 0.0166, 1):
                        motor.motor_go(False, "Full", 1, deceleration, 0)
                        motor1.motor_go(True, "Full", 1, deceleration, 0)

                time.sleep(1)
        
        if input == True:
            sys.exit("Emergency Button Pressed")

