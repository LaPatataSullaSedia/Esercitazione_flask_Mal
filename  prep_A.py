import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Animali")
mycursor.execute("USE Animali")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Mammiferi (
        Id INT AUTO_INCREMENT PRIMARY KEY,
        Nome_Proprio VARCHAR(255),
        Razza VARCHAR(255),
        Peso INT,
        Eta INT
    )
""")
print("Database e tabella creati correttamente.")
