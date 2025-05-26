
import mysql.connector
from flask import Flask

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/air_transport")
def airTransport():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE trasporto = 'Air'")
    rows = mycursor.fetchall()
    return jsonify(rows)

@app.route("/epic_units")
def epicUnits():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE rarita = 'epic'")
    rows = mycursor.fetchall()
    return jsonify(rows)

@app.route("/high_cost_units")
def highCost():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE costo > 4")
    rows = mycursor.fetchall()
    return jsonify(rows)

@app.route("/ground_units")
def groundUnits():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE trasporto = 'Ground'")
    rows = mycursor.fetchall()
    return jsonify(rows)



@app.route("/getAllDataInHtml")
def getAllData():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(x);
    return result