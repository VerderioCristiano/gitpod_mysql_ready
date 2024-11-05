
import mysql.connector



# Creare una connessione al database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"
)

mycursor = mydb.cursor()



mycursor.execute("SELECT * FROM mammiferi WHERE peso > 2")


# Salvare (commit) le modifiche

myresult = mycursor.fetchall()
for x in myresult:
    print(x)



