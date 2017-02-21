#!/usr/bin/env python
"""
	Detects motion and pings node server about availability.
"""

import RPi.GPIO as GPIO
import time
import urllib2

__author__ = "gus-pimylifeup"
__version__ = "1.0"
__maintainer__ = "pimylifeup.com"

pir_sensor = 11
piezo = 7

GPIO.setmode(GPIO.BOARD)

GPIO.setup(piezo,GPIO.OUT)

GPIO.setup(pir_sensor, GPIO.IN)

current_state = 0
try:
    while True:
        time.sleep(1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print("There is movement around sensor")
            GPIO.output(piezo,True)
            urllib2.urlopen("http://slashping.narvar.qa/status?available=false").read()
        if current_state == 0:
            print("No movement detected")
            GPIO.output(piezo,False)
            urllib2.urlopen("http://slashping.narvar.qa/status?available=true").read()
except KeyboardInterrupt, HTTPError:
    print("Server Error")
    pass
finally:
    GPIO.cleanup()
