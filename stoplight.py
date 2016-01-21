import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
for x in range (0,20):
    GPIO.output(7, True)
    print '7 on'
    time.sleep(1) 
    GPIO.output(7, False)
    print '7 off'
    GPIO.output(11, True)
    print '11 on'
    time.sleep(1) 
    GPIO.output(11, False)
    print '11 off'
    GPIO.output(15, True)
    print '15 on'
    time.sleep(1) 
    GPIO.output(15, False)
    print '15 off'
GPIO.cleanup()
