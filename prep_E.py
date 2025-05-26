import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="Animali"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Mammiferi WHERE Peso > 2")

for animale in mycursor.fetchall():
    print(animale)
