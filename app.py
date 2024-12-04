from flask import Flask
from flask_cors import CORS  # Importa il modulo per CORS
from routes.routes import routes
from models.model import Model

app = Flask(__name__) # Configurazione dell'app Flask
CORS(app)  # Abilita CORS per l'intera app
app.register_blueprint(routes, url_prefix='/api') # Registra il Blueprint per le route


# DB_PATH = "database/example.db" # Percorso del database
# def initialize_database(): # Funzione di inizializzazione del database
#     db = Model(DB_PATH)
#     db.create_table("table_name", {
#         "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
#         "name": "TEXT",
#         "email": "TEXT"
#     })
#     print("Tabella 'table_name' inizializzata con successo.")
# initialize_database() # Inizializza il database all'avvio dell'app


if __name__ == '__main__':
    print("Avviando il server Flask...")
    app.run(debug=True)


# Esempio di utilizzo:
# Avvia il server con `python app.py`
# Testa l'app con un endpoint eseguendo:
# GET: http://localhost:5000/api/<nome_tabella>
# POST: http://localhost:5000/api/<nome_tabella> con JSON {"col1": "valore1", "col2": "valore2"}
