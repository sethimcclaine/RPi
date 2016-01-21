import RPi.GPIO as GPIO
import sys

led = int(sys.argv[1])

if sys.argv[2] == '1':
    switch = True
else: 
    switch = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, switch)

