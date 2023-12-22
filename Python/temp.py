# Setup
# `sudo pip3 install w1thermsensor`

# Code: https://bigl.es/ds18b20-temperature-sensor-with-python-raspberry-pi/#:~:text=The%20yellow%20jumper%20cable%20goes,pin%20to%20the%20MIDDLE%20pin.

# Turn on singlewire
# `sudo raspi-config`
# -> `#3 Interface Options` -> `#I7 1-Wire` -> `<Yes>`
# Check for singlewire device...
# `ls /sys/bus/w1/devices`
# should be a `28-xxxxxx` device, if not probably not hooked up correctly
## Example missing the 4.7k (10k will also work) resister, see diagram
# Diagram: https://forums.raspberrypi.com/viewtopic.php?t=207261#p1282383

import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    print("The temperature is %s celsius" % temperature)
    time.sleep(1)
