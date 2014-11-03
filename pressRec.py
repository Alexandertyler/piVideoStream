#!/usr/bin/env python
#Button press starts video for 5 seconds

import RPi.GPIO as GPIO
import time
import subprocess
import psutil
import os

channel = 17
PROCNAME = "raspivid"

def runCam(channel):
    piVid = subprocess.Popen(["raspivid",  "-o",  "-", "-t"," 0", "-w", "640", "-h", "480", "-fps", "25", "-b", "2000000", "-g", "50"], stdout=subprocess.PIPE)
    ffmpeg = subprocess.Popen(["/home/pi/arm/bin/ffmpeg", "-re", "-ar", "44100", "-ac", "2", "-acodec", "pcm_s16le", "-f", "s16le", "-ac", "2", "-i", "/dev/zero", "-f", "h264", "-i", "-", "-vcodec", "copy", "-acodec", "aac", "-ab", "128k", "-g", "50", "-strict", "experimental", "-f", "flv", "rtmp://a.rtmp.youtube.com/live2/shunshou.pyf1-dvt8-vdm5-8d02"], stdin=piVid.stdout)
    print "runCam called"
        
def camKill(channel):
    print "He's dead Jim"

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(channel, GPIO.FALLING, bouncetime=3000)
GPIO.add_event_callback(channel, runCam)

#GPIO.wait_for_edge(17, GPIO.FALLING)
#piVid = subprocess.Popen(["raspivid",  "-o",  "-", "-t"," 0", "-w", "640", "-h", "480", "-fps", "25", "-b", "500000", "-g", "50"], stdout=subprocess.PIPE)
#subprocess.Popen([ ./ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/shunshou.b25p-r6vx-adac-8kc9"], shell=True)
#for line in piVid.stdout:
#    print line
#time.sleep(2)
#GPIO.wait_for_edge(17, GPIO.FALLING)
#for proc in psutil.process_iter():
#    if proc.name() == PROCNAME:
#         proc.kill()

while True:
    time.sleep(0.1)
