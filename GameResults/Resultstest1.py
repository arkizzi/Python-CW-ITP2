import mysql.connector
from mysql.connector import Error

#Open database connection with a dictionary
conDict = {'host':'localhost',
           'database':'game_records',
           'user':'root',
           'password':''}
db = mysql.connector.connect(**conDict)

#preparing cursor
cursor = db.cursor()

#executing SQL query
myInsertText = "INSERT INTO tbl_game_score VALUES (12341,'Me,'Easy',10,50)"
cursor.execute(myInsertText)

#Commit
db.commit()
print(cursor.rowcount,"Record Added")

#Disconnect
db.close()
