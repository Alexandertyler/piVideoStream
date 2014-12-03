#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import subprocess
import psutil
import os
import urllib2
import json
import sys

# Button on GPIO 18
channel = 16

# Action when button pressed
def readCompass(channel):

# Setup button GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(channel, GPIO.FALLING, bouncetime=3000)
GPIO.add_event_callback(channel, runCam)

while True:
    time.sleep(0.1)
