import sqlite3
import time
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import re
from datetime import datetime, timedelta
import http
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('jrad.sqlite')
cur = conn.cursor()

baseurl = 'https://api.setlist.fm/rest/1.0/artist/84a69823-3d4f-4ede-b43f-17f85513181a/setlists?p=2'
    
parms = {'Accept': 'application/json', 'x-api-key': 'ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK'}

#r = requests.get(url = url, parms = parms)

while true:
    url = baseurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1
    
    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue
    
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break