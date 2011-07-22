#!/usr/bin/python
import sys
import httplib
import json
import time

forrstid = sys.argv[1]
server = httplib.HTTPSConnection('forrst.com')
server.request('GET','/api/v2/users/info?username=%s' % forrstid)
response = server.getresponse()
jsonstr = response.read()
userobj = json.loads(jsonstr)
forrstid =  userobj['resp']['id']
print forrstid
