import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"

for i in range(5):
    print(f"\nInserimento animale {i + 1}:")
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
print("Inserimento completato.")
