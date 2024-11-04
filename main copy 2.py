#mostra la prima riga che soddisfa i requisiti del SELECT

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM mammiferi")

myresult = mycursor.fetchall()

print(myresult)