import json
import urllib2

def do_request(authenticator, method, path, data = {}):
	request = urllib2.Request(url='https://coinbase.com/api/v1' + path, data=json.dumps(data) if data else None)
	request.headers.update(authenticator.get_headers(request))

	f = urllib2.urlopen(request)

	return json.loads(f.read())