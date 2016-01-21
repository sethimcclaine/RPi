**LED.py**
- Turn specified light on and off 20 times
- _Light is specified in code_
- `sudo python LED.py`

-----------------------------

**cmdLED.py**

- Turn given light on or off (uses user input)
- _Utilizes 1 of 8 lights_
- `sudo python cmdLED.py 11 1` (On)
- `sudo python cmdLED.py 7 0` (Off)
- **NOTE:** Does not do a GPIO.cleanup causing errors to throw (This is on purpose to leave light on/off after program is complete)

-----------------------------

**binary60.py**
- Count from 0 - 60 in binary
- _Utilizes 8 of 8 leds_
- `sudo python binary60.py`

