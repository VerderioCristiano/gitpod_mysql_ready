#creare database

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Animali")
mycursor.execute("CREATE TABLE mammiferi ( id INT AUTO_INCREMENT PRIMARY KEY, Nome_Proprio VARCHAR(255), razza VARCHAR(255), peso INT, eta INT)")