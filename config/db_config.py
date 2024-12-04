import os

class DBConfig:
    """Gestisce la configurazione del database."""
    def __init__(self, path=".", name="example.db"):
        if not os.path.isdir(path):
            os.makedirs(path, exist_ok=True)
        self.path = path
        self.name = name

    @property
    def full_path(self):
        return os.path.join(self.path, self.name)

# Esempio di utilizzo:
# config = DBConfig(path="data", name="my_database.db")
# print(config.full_path)  # Stampa il percorso completo del database
