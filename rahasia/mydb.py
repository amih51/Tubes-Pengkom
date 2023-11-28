import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'user',

)

# prepare cursor
cursorObject = dataBase.cursor()
# create database
cursorObject.execute("CREATE DATABASE movieXIV")

print("Done!")







