#!/usr/bin/env python

import urllib2
import json
import sys
import os

class jsonComm:

	streamId = ""
	ytId = "123456"
	#these should be static
	baseUrl = "https://contextualvideo-shunshou.rhcloud.com/"
	mac = "01:02:03:04:05:06"
	
	def getYtPost(self):
		url = self.baseUrl + "pi_getYT_3"
		data = { "mac" : self.mac }
		req = urllib2.Request(url)
		req.add_header('Content-Type', 'application/json')
		response = urllib2.urlopen(req, json.dumps(data))
		returnJson = response.read()
		print "Returned Json is " + returnJson
		decodedJson = json.loads(returnJson)
		self.streamId = decodedJson["id"]
		self.ytId = decodedJson["ytid"]
	
	def piStreamPost(self, flag, compass):
		#flag options are start, append or done
		url = self.baseUrl + "pi_" + flag + "_context"
		data = { "id" : self.streamId, 
				 "compass" : compass,
				 "time_offset" : "0",
				 "date_offset" : "0" }
		req = urllib2.Request(url)
		req.add_header('Content-Type', 'application/json')
		response = urllib2.urlopen(req, json.dumps(data))
		print response.read()

