
import sqlite3
import mysql.connector



# Creare una connessione al database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"
)

mycursor = mydb.cursor()

def chiedi_animale():
    nome = input("Inserisci il nome dell'animale: ")
    razza = input("Inserisci il tipo di animale (ad esempio, cane, gatto, ecc.): ")
    eta = chiedi_intero("Inserisci l'età dell'animale (numero intero): ")
    peso = chiedi_intero("Inserisci il peso dell'animale (numero intero): ")
    return {"nome": nome, "razza": razza, "eta": eta, "peso": peso}



def inserisci_animali():
    animali = []
    for i in range(5):
        print(f"\nInserisci i dati per l'animale {i+1}:")
        animale = chiedi_animale()

        try:
            int(animale.eta) or int(animale.peso)  # Prova a convertire l'input in un intero
            print(f"hai inserito un animale.")
        except ValueError:  # Se fallisce la conversione, non è un intero
            print(f"hai sbagliato ad inserire dei numeri.")


        animali.append(animale)
        continua = input("Vuoi inserire un altro animale? (sì/no): ").strip().lower()
        if continua != 'sì':
            break
    return animali



insert_query = '''
INSERT INTO mammiferi (nome_proprio, razza, peso, eta) VALUES ( %s, %s, %s, %s)
'''


mycursor.executemany(inserisci_animali(), insert_query)
mycursor.execute()


# Salvare (commit) le modifiche
mydb.commit()


# Chiudere la connessione
mycursor.close()
mydb.close()


