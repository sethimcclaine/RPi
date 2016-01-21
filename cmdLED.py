import RPi.GPIO as GPIO
import sys
import time

led = int(sys.argv[1])

lights = [7,11,15]
lights.remove(led)

if sys.argv[2] == '1':
    switch = True
else: 
    switch = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.output(led, switch)

for x in range (0,20):
    GPIO.output(int(lights[0]), True)
    GPIO.output(int(lights[1]), True)
    time.sleep(.1) 
    GPIO.output(int(lights[0]), False)
    GPIO.output(int(lights[1]), False)
    time.sleep(.1) 

GPIO.cleanup()
