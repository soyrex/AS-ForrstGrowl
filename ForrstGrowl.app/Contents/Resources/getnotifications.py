#!/usr/bin/python
import sys
import httplib
import json
import time

forrstid = sys.argv[1]
nexturl = '/feed/poll?u=%s' % forrstid
pollserver = httplib.HTTPSConnection('forrst.com')
pollserver.request('GET',nexturl)
data = pollserver.getresponse().read().strip()

if data != "0":
    print "You have %s notifications." % data
