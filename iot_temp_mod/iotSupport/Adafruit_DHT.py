import sys

import Adafruit_DHT
import time

def read_retry(sensorVersion,GPIOpin):
    outTime =int(time.time())
    time.sleep(.5)
    humidity = 39.0
    temperature = 45.0
    return humidity, temperature, outTime
