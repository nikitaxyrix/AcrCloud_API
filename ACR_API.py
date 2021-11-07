import argparse
import base64
import hashlib
import hmac
import os
import sys
import time
import requests

def init(access, secret, userequrl = False, url = 'https://identify-eu-west-1.acrcloud.com/v1/identify'):
	global access_key
	access_key = access
	global access_secret
	access_secret = secret
	global requrl
	if userequrl == True:
		requrl = url
	else:
		requrl = 'https://identify-eu-west-1.acrcloud.com/v1/identify'
	global http_method
	http_method = "POST"
	global http_uri
	http_uri = "/v1/identify"
	global data_type
	data_type = "audio"
	global signature_version
	signature_version = "1"
	global timestamp
	timestamp = time.time()
	global string_to_sign
	string_to_sign = http_method + "\n" + http_uri + "\n" + access_key + "\n" + data_type + "\n" + signature_version + "\n" + str(timestamp)
	global sign
	sign = base64.b64encode(hmac.new(access_secret.encode('ascii'), string_to_sign.encode('ascii'), digestmod=hashlib.sha1).digest()).decode('ascii')
def recognize(filename):
	f = open(filename, 'rb')
	sample_bytes = os.path.getsize(filename)
	files = [
    ('sample', (filename, open(filename, 'rb'), 'audio/mpeg'))
	]
	try:
		data = {
			'access_key': access_key,
       	'sample_bytes': sample_bytes,
       	'timestamp': str(timestamp),
       	'signature': sign,
       	'data_type': data_type,
       	"signature_version": signature_version
	}
	except:
		print('You forgot to use init() !')
		sys.exit(0)
	r = requests.post(requrl, files=files, data=data)
	r.encoding = "utf-8"
	return r.text