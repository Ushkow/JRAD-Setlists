import setlist_fm_client
import re
import sqlite3

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=9, api_key=xxxxxxx, serialize=True)

#Collecting the direct url link to setlist page for each show. Then will use beautiful soup to parse each setlist page to collect and store in database: date, city, venue, songs. 

conn = sqlite3.connect('jrad.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Setlists
    (url TEXT UNIQUE)''')

#The API and setlist_fm_client function only allow us to call one page of results.
#Until I find a more elegant workaround, I am adding code to collect from each page by updating the parameter--p--in the function call.
#In earlier iterations of this code I retrieved the urls from the first 8 pages of setlist data. 


lst = list()
x = "https://www.setlist.fm/setlist/"
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst.append(item[13:])
        for show in lst:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
        
#The API and setlist_fm_client function only allow us to call one page of results.
#Until I find a more elegant workaround, I am adding code to collect from each page by updating the parameter--p--in the function call.
#In earlier iterations of this code I retrieved the urls from the first 8 pages of setlist data. 



setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=10, api_key=xxxxxxx, serialize=True)
lst2 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst2.append(item[13:])
        for show in lst2:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
        

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=11, api_key=xxxxxxx, serialize=True)
lst3 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst3.append(item[13:])
        for show in lst3:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()


print('done')
                            

    
