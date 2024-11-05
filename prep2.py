
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
INSERT INTO mammiferi (nome_proprio, razza, peso, eta) VALUES ( %s, %s, %s, %s)
'''

# Dati degli animali
animali = [
    ( 'Mia', 'Gatto Persiano', 4, 4),
    ( 'Nemo', 'Pesce Pagliaccio', 0, 2),
    ('Polly', 'Pappagallo', 1, 5),
    ( 'Whiskers', 'Coniglio Angora', 2, 3),
    ( 'Tigro', 'Furetto', 1, 1)
]

# Eseguire l'inserimento

mycursor.executemany(insert_query, animali)


#mycursor.execute("SELECT * FROM mammiferi")
# Salvare (commit) le modifiche
mydb.commit()


# Chiudere la connessione
mycursor.close()
mydb.close()


