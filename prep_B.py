import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="Animali"
)

mycursor = mydb.cursor()

animali = [
    ("Fido", "Labrador", 30, 5),
    ("Milo", "Beagle", 12, 3),
    ("Tigro", "Gatto Europeo", 4, 2),
    ("Leo", "Maine Coon", 6, 4),
    ("Nina", "Bassotto", 8, 6)
]

sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
mycursor.executemany(sql, animali)

mydb.commit()
print(mycursor.rowcount, "animali inseriti.")
