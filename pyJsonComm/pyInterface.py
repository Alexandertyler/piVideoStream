#!/usr/bin/env python
import pyJsonComm
import time

def main():
	mJsonComm = pyJsonComm.jsonComm()
	print "jsonComm object created"
	mJsonComm.getYtPost()
	print "GetytPost successful"
	i = 0
	#mJsonComm.piStreamPost("start", str(i))
	#while i < 100:
	#	mJsonComm.piStreamPost("append", str(i))
	#	time.sleep(20)
	#	i += 1
	mJsonComm.piStreamPost("done", str(i+1))

if __name__ == "__main__":
	main()
