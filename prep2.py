
import sqlite3
import mysql.connector

import mysql.connector

# Creare una connessione al database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"
)

mycursor = mydb.cursor()

# Query di inserimento in una variabile
insert_query = '''
INSERT INTO mammiferi (id, nome_proprio, razza, peso, eta) VALUES (%s, %s, %s, %s, %s)
'''

# Dati degli animali
animali = [
    (1, 'Mia', 'Gatto Persiano', 4.0, 4),
    (2, 'Nemo', 'Pesce Pagliaccio', 0.1, 2),
    (3, 'Polly', 'Pappagallo', 1.2, 5),
    (4, 'Whiskers', 'Coniglio Angora', 2.3, 3),
    (5, 'Tigro', 'Furetto', 1.5, 1)
]

# Eseguire l'inserimento

mycursor.executemany(insert_query, animali)


mycursor.execute("SELECT * FROM mammiferi")
# Salvare (commit) le modifiche
mydb.commit()


# Chiudere la connessione
mycursor.close()
mydb.close()


