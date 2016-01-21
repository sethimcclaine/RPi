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

output = board[0] 

sleepLength = .1

GPIO.setup(output, GPIO.OUT)
for x in range (0,20):
    GPIO.output(output, True)
    time.sleep(sleepLength)
    GPIO.output(output, False)
    time.sleep(sleepLength)
GPIO.cleanup()
