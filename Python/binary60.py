'''
Count from 0 to 60 
light up the leds representing the binary number
'''

import RPi.GPIO as GPIO
import time

'''
#Board Number
GPIO.setmode(GPIO.BOARD)
board = [7, 11, 12, 13, 15, 16, 18, 22]
'''
#Output Number
GPIO.setmode(GPIO.BCM)
board = [4, 17, 18, 27, 22, 23, 24, 25]

for x in range (0,8):
    GPIO.setup(board[x], GPIO.OUT)
for x in range (0,61):
    time.sleep(.25)
    y = x
 
    if y == 60:
        for z in range (0,6):
            GPIO.output(board[z], False)
        for x in range (0,4):
            GPIO.output(board[6], True)
            GPIO.output(board[7], True)
            time.sleep(.25)
            GPIO.output(board[6], False)
            GPIO.output(board[7], False)
            time.sleep(.25)      

    if y/32 > 0:
        y = y % 32
        GPIO.output(board[5], True)
    else:
        GPIO.output(board[5], False)

    if y/16 > 0:
        y = y %16 
        GPIO.output(board[4], True)
    else:
        GPIO.output(board[4], False)

    if y/8 > 0:
        y = y % 8
        GPIO.output(board[3], True)
    else:
        GPIO.output(board[3], False)

    if y/4 > 0:
        y = y % 4
        GPIO.output(board[2], True)
    else:
        GPIO.output(board[2], False)

    if y/2 > 0:
        y = y % 2
        GPIO.output(board[1], True)
    else:
        GPIO.output(board[1], False)

    if y/1 > 0:
        GPIO.output(board[0], True)
    else:
        GPIO.output(board[0], False)
 

GPIO.cleanup()
