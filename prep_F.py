import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="Animali"
)

mycursor = mydb.cursor()
sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"

try:
    num_animali = int(input("Quanti animali vuoi inserire? "))
except ValueError:
    print("Errore: Inserire un numero valido.")
    exit()

for i in range(num_animali):
    print(f"\nAnimale {i+1}:")
    nome = input("Nome: ")
    razza = input("Razza: ")
    try:
        peso = int(input("Peso (kg): "))
        eta = int(input("Età: "))
    except ValueError:
        print("Errore: Peso ed Età devono essere numeri interi.")
        continue
    mycursor.execute(sql, (nome, razza, peso, eta))

mydb.commit()
print(f"{num_animali} animali inseriti.")
