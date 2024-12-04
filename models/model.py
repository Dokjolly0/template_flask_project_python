import sqlite3

class Model:
    def __init__(self, db_path):
        self.db_path = db_path

    def connect(self):
        """Crea una connessione al database SQLite."""
        return sqlite3.connect(self.db_path, check_same_thread=False)

    def create_table(self, table_name, fields):
        """Crea una tabella con i campi specificati."""
        field_definitions = ", ".join([f"{name} {type}" for name, type in fields.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({field_definitions})"
        with self.connect() as conn:
            conn.execute(query)

    def insert(self, table_name, data):
        """Inserisce un record nella tabella."""
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        with self.connect() as conn:
            conn.execute(query, tuple(data.values()))

    def fetch_all(self, table_name):
        """Ottiene tutti i record dalla tabella."""
        query = f"SELECT * FROM {table_name}"
        with self.connect() as conn:
            return conn.execute(query).fetchall()

    def update(self, table_name, data, condition):
        """Aggiorna i record nella tabella con la condizione specificata."""
        set_clause = ", ".join([f"{key} = ?" for key in data.keys()])
        where_clause = " AND ".join([f"{key} = ?" for key in condition.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
        with self.connect() as conn:
            conn.execute(query, tuple(data.values()) + tuple(condition.values()))

    def delete(self, table_name, condition):
        """Elimina i record dalla tabella con la condizione specificata."""
        where_clause = " AND ".join([f"{key} = ?" for key in condition.keys()])
        query = f"DELETE FROM {table_name} WHERE {where_clause}"
        with self.connect() as conn:
            conn.execute(query, tuple(condition.values()))

# Esempio di utilizzo:
# model = Model("database/example.db")
# model.create_table("users", {"id": "INTEGER PRIMARY KEY", "name": "TEXT"})
# model.insert("users", {"id": 1, "name": "John"})
# print(model.fetch_all("users"))
