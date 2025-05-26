import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="Animali"
    )

def inserisci_animale():
    nome = input("Nome: ")
    razza = input("Razza: ")
    try:
        peso = int(input("Peso: "))
        eta = int(input("Età: "))
    except ValueError:
        print("Errore: peso ed età devono essere interi.")
        return
    cursor.execute("INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)", (nome, razza, peso, eta))
    db.commit()
    print("Animale inserito.")

def visualizza_animali():
    cursor.execute("SELECT * FROM Mammiferi")
    for animale in cursor.fetchall():
        print(animale)

def elimina_animale():
    id = input("ID dell'animale da eliminare: ")
    cursor.execute("DELETE FROM Mammiferi WHERE Id = %s", (id,))
    db.commit()
    print("Animale eliminato.")

def modifica_animale():
    id = input("ID dell'animale da modificare: ")
    nome = input("Nuovo nome: ")
    razza = input("Nuova razza: ")
    try:
        peso = int(input("Nuovo peso: "))
        eta = int(input("Nuova età: "))
    except ValueError:
        print("Errore: peso ed età devono essere interi.")
        return
    cursor.execute("UPDATE Mammiferi SET Nome_Proprio=%s, Razza=%s, Peso=%s, Eta=%s WHERE Id=%s",
                   (nome, razza, peso, eta, id))
    db.commit()
    print("Animale modificato.")

# MAIN
db = connect_db()
cursor = db.cursor()

while True:
    print("\n--- MENU ---")
    print("1. Inserisci un nuovo animale")
    print("2. Visualizza tutti gli animali")
    print("3. Elimina un animale")
    print("4. Modifica un animale")
    print("5. Esci")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        inserisci_animale()
    elif scelta == "2":
        visualizza_animali()
    elif scelta == "3":
        elimina_animale()
    elif scelta == "4":
        modifica_animale()
    elif scelta == "5":
        print("Uscita dal programma.")
        break
    else:
        print("Scelta non valida.")
