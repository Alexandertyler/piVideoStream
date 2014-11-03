#!/usr/bin/env python
#Button press starts video for 5 seconds

import RPi.GPIO as GPIO
import time
import subprocess
import psutil

PROCNAME1 = "ffmpeg"


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)



while true:
    GPIO.wait_for_edge(17, GPIO.FALLING)
    subprocess.call(['bash ~/arm/bin/raspivid_wifi_to_youtube.sh'])
    GPIO.wait_for_edge(17, GPIO.FALLING)
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()
    
