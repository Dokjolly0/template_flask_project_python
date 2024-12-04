from flask import Blueprint, request, jsonify
from models.model import Model
import os

routes = Blueprint('routes', __name__)
db_path = os.getenv('DB_PATH', 'database/example.db')
db_model = Model(db_path)

# Endpoint per ottenere tutti i record di una tabella
@routes.route('/table_name', methods=['GET'])
def fetch_all():
    data = db_model.fetch_all('table_name')
    return jsonify(data), 200

# Endpoint per inserire un record in una tabella
@routes.route('/table_name', methods=['POST'])
def insert_data():
    data = request.get_json()
    db_model.insert('table_name', data)
    return jsonify({"message": "Data inserted successfully"}), 201

# Esempio di utilizzo:
# Importa le rotte nel file principale `app.py` e registra il Blueprint.
# Testa le rotte con:
# GET: http://localhost:5000/api/<table_name>
# POST: http://localhost:5000/api/<table_name> con JSON {"col1": "valore1"}
