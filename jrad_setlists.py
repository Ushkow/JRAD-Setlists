import setlist_fm_client
import re
import sqlite3

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=9, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)

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



setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=10, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
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
        

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=11, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
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
        

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=12, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst4 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst4.append(item[13:])
        for show in lst4:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
        

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=13, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst5 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst5.append(item[13:])
        for show in lst5:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
                

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=14, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst6 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst6.append(item[13:])
        for show in lst6:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()


setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=15, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst7 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst7.append(item[13:])
        for show in lst7:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
                

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=16, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst8 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst8.append(item[13:])
        for show in lst8:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
    

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=17, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst9 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst9.append(item[13:])
        for show in lst9:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
                

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=18, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst10 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst10.append(item[13:])
        for show in lst10:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
        

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=19, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst11 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst11.append(item[13:])
        for show in lst11:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
        

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=20, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst12 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst12.append(item[13:])
        for show in lst12:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
        

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=21, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst13 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst13.append(item[13:])
        for show in lst13:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
                

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=22, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst14 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst14.append(item[13:])
        for show in lst14:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()


setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=23, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst15 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst15.append(item[13:])
        for show in lst15:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
                

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=24, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst16 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst16.append(item[13:])
        for show in lst17:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
    

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=25, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst18 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst18.append(item[13:])
        for show in lst18:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
                

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=26, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst19 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst19.append(item[13:])
        for show in lst19:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
        

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=27, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst20 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst20.append(item[13:])
        for show in lst20:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
        

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=28, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst21 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst21.append(item[13:])
        for show in lst21:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
                

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=29, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst22 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst22.append(item[13:])
        for show in lst22:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()

setlists = setlist_fm_client.get_artist_setlists("84a69823-3d4f-4ede-b43f-17f85513181a", p=30, api_key="ysirQRa-QGBbI0bS3fNoGg4s-LLDmWbR5KqK", serialize=True)
lst23 = list()
data = str(setlists)
lines = data.split()
for item in lines:
    if x in item:
        lst23.append(item[13:])
        for show in lst23:
            if len(show) > 1:
                cur.execute('INSERT OR IGNORE INTO Setlists (url) VALUES ( ? )', ( show, ) )
                conn.commit()
                
print('done')
                            

    
