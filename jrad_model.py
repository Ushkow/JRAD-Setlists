import sqlite3
import time
import re
import zlib
from datetime import datetime, timedelta

#Code will clean up the urls in Setlists table containing direct url linking to each JRAD setlist.
#Then will visit each link and get date, city, venue and song data for each setlist.

#def fixurl(
#    K = 2
#    link = str.rstrip(s[:K]) for s in link
#)

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Setlists ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Setlists
    (url TEXT UNIQUE)''')

conn_1 = sqlite3.connect('file:jrad.sqlite?mode=ro', uri=True)
cur_1 = conn_1.cursor()

setlist_urls = list()
cur_1.execute('''SELECT url FROM Setlists''')
for setlists_row in cur_1 :
    fixurl = setlists_row[0]
    fixurl = fixurl[:-2]
    setlist_urls.append(fixurl)
    
print("Loaded urls", len(setlist_urls))

for item in setlist_urls:
    print(item)
    cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( item, ) )
    conn.commit()

cur.close()
cur_1.close()