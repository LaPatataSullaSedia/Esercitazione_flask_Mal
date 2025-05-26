import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='mydatabase'
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS CLASH_ROYALE")

mycursor.execute("""
  CREATE TABLE IF NOT EXISTS CLASH_ROYALE.Clash_Unit (
    Unit VARCHAR(30) NOT NULL,
    Cost INTEGER,
    Hit_Speed VARCHAR(30),
    Speed VARCHAR(30),
    Deploy_Time VARCHAR(30),
    Range_ VARCHAR(30),
    Target VARCHAR(30),
    Count VARCHAR(30),
    Transport VARCHAR(30),
    Type VARCHAR(30),
    Rarity VARCHAR(30),
    PRIMARY KEY (Unit)
  );""")

mycursor.execute("DELETE FROM CLASH_ROYALE.Clash_Unit")
mydb.commit()

clash_data = pd.read_csv('./cr-unit-attributes.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))

for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    sql = "INSERT INTO CLASH_ROYALE.Clash_Unit VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    mydb.commit()

mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)