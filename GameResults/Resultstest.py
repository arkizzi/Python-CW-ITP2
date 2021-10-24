import mysql.connector

#Open database connection with a dictionary
mydb = mysql.connector.connect(
    host = "localhost",
    user = "localhost",
    password = "",
    database = "game_records"
)

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
