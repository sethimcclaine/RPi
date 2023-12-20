import RPi.GPIO as GPIO
import time

a = 7
b = 11
c = 12
d = 13
e = 15
f = 16
g = 18
h = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(f, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(h, GPIO.OUT)
for x in range (0,20):
    GPIO.output(a, True)
    time.sleep(.1) 
    GPIO.output(a, False)
    GPIO.output(b, True)
    time.sleep(.1) 
    GPIO.output(b, False)
    GPIO.output(c, True)
    time.sleep(.1) 
    GPIO.output(c, False)
    GPIO.output(d, True)
    time.sleep(.1) 
    GPIO.output(d, False)
    GPIO.output(e, True)
    time.sleep(.1) 
    GPIO.output(e, False)
    GPIO.output(f, True)
    time.sleep(.1) 
    GPIO.output(f, False)
    GPIO.output(g, True)
    time.sleep(.1) 
    GPIO.output(g, False)
    GPIO.output(h, True)
    time.sleep(.1) 
    GPIO.output(h, False)
GPIO.cleanup()
