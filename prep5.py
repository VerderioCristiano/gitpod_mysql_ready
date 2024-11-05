from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Funzione per connettersi al database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Animali"
    )

# Rotta per ottenere il contenuto della tabella 'mammiferi' in formato JSON
@app.route('/api/mammiferi', methods=['GET'])
def get_mammiferi():
    # Connessione al database
    mydb = connect_to_db()
    mycursor = mydb.cursor(dictionary=True)
    
    # Esecuzione della query per selezionare tutti i dati dalla tabella
    mycursor.execute("SELECT * FROM mammiferi")
    mammiferi = mycursor.fetchall()
    
    # Chiusura delle connessioni
    mycursor.close()
    mydb.close()
    
    # Restituisce i dati in formato JSON
    return jsonify(mammiferi)

@app.route('/api/mammiferi', methods=['POST'])
def add_mammifero():
    data = request.get_json()  # Recupera i dati JSON inviati dal client

    # Verifica che tutti i campi necessari siano presenti
    if not all(key in data for key in ('nome_proprio', 'razza',  'peso', 'eta')):
        return jsonify({"error": "Dati mancanti"}), 400

    nome = data['nome_proprio']
    razza = data['razza']
    peso = data['peso']
    eta = data['eta']

    # Connessione al database e inserimento dei dati
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    sql = "INSERT INTO mammiferi (nome_proprio, razza, peso, eta) VALUES (%s, %s, %s, %s)"
    values = (nome, razza, peso, eta)
    mycursor.execute(sql, values)
    mydb.commit()

    mycursor.close()
    mydb.close()

    return jsonify({"message": "Animale inserito con successo!"}), 201

@app.route('/api/mammiferi/<int:id>', methods=['PUT'])
def update_mammifero(id):
    data = request.get_json()

    # Verifica che tutti i campi necessari siano presenti
    if not all(key in data for key in ('nome_proprio', 'razza',  'peso', 'eta')):
        return jsonify({"error": "Dati mancanti"}), 400

    nome = data['nome_proprio']
    razza = data['razza']
    peso = data[ 'peso']
    eta = data['eta']

    # Connessione al database e aggiornamento dei dati
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    sql = "UPDATE mammiferi SET nome_proprio = %s, razza = %s, peso = %s, eta = %s WHERE Id = %s"
    values = (nome, razza, peso, eta, id)
    mycursor.execute(sql, values)
    mydb.commit()

    mycursor.close()
    mydb.close()

    # Controlla se l'update ha modificato delle righe
    if mycursor.rowcount == 0:
        return jsonify({"message": "Animale non trovato"}), 404

    return jsonify({"message": "Animale aggiornato con successo!"}), 200

@app.route('/api/mammiferi/<int:id>', methods=['DELETE'])
def delete_mammifero(id):
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    # Verifica se l'animale con questo id esiste
    mycursor.execute("SELECT * FROM mammiferi WHERE Id = %s", (id,))
    if not mycursor.fetchone():
        mycursor.close()
        mydb.close()
        return jsonify({"message": "Animale non trovato"}), 404

    # Esegue l'operazione di DELETE
    sql = "DELETE FROM mammiferi WHERE Id = %s"
    mycursor.execute(sql, (id,))
    mydb.commit()

    mycursor.close()
    mydb.close()

    return jsonify({"message": "Animale eliminato con successo!"}), 200


if __name__ == '_main_':
    app.run(debug=True)