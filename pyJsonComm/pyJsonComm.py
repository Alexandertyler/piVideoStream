#!/usr/bin/env python

import urllib2
import json
import sys
import os

class jsonCommRpi:
	streamId = ""
	ytId = ""
	#these should be static
	baseUrl = "https://contextualvideo-shunshou.rhcloud.com"
	mac = ""
	

    def getYtPost(self):
		url = self.baseUrl + "/pi_getYT_3"
		data = { "mac" : self.mac }

		req = urllib2.Request(url)
		req.add_header('Content-Type', 'application/json')
		response = urllib2.urlopen(req, json.dumps(data))
		returnJson = response.read()
		print returnJson
		decodedJson = json.loads(returnJson)
		self.streamId = decoded["stream_id"]
		self.ytId = decoded["youtube_id"
	
	def piStreamPost(self, flag, compass):
		#flag options are /append or /stop
		url = self.baseUrl + flag
		data = { "id" : self.streamId, 
				 "compass" : compass,
				 "time_offset" : "0",
				 "date_offset" : "0" }
		req = urllib2.Request(url)
		req.add_header('COntent-Type', 'application/json')
		response = urllib2.urlopen(req, json.dumps(data))
		print response

