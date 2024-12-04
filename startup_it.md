# Flask Project Setup

Questo è un template per un'applicazione web basata su Flask con SQLite come database. Questa guida ti guiderà attraverso il processo di configurazione del progetto, l'installazione delle dipendenze e l'avvio dell'applicazione.

## Prerequisiti

Prima di iniziare, assicurati di avere installato quanto segue sul tuo computer:

- [Python 3.7+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

## Step 1: Clona il Repository

Prima di tutto, clona il repository sul tuo computer.

```bash
git clone https://github.com/yourusername/template_flask_project_python.git
cd template_flask_project_python
```

## Step 2: Crea un Ambiente Virtuale

Un ambiente virtuale isola le dipendenze del tuo progetto dall'ambiente Python globale. È una buona pratica crearne uno per ciascun progetto.

```bash
python -m venv venv
```

### Step 3: Attiva l'Ambiente Virtuale

- **Windows:**

```bash
venv\Scriptsctivate
```

- **macOS/Linux:**

```bash
source venv/bin/activate
```

Una volta attivato l'ambiente virtuale, il tuo terminale dovrebbe mostrare `(venv)` prima del prompt.

## Step 4: Installa le Dipendenze

Installa le librerie Python richieste utilizzando il comando `pip`. Assicurati che il tuo ambiente virtuale sia attivato quando lo fai.

```bash
pip install -r requirements.txt
```

Questo installerà le seguenti librerie (e le relative dipendenze):

- `Flask`: Web framework for Python.
- `Flask-CORS`: Handle Cross-Origin Resource Sharing (CORS).
- `SQLite3`: Embedded database for Python.

## Step 5: Configurazione del Database

Il progetto utilizza SQLite come database. Se desideri inizializzare manualmente il database, puoi utilizzare il metodo fornito nel file `app.py`:

Se vuoi inizializzare manualmente il database, puoi utilizzare il metodo fornito nel file `app.py`:

```python
initialize_database()
```

Questo metodo creerà un database SQLite chiamato `example.db` con una tabella di esempio chiamata `users`.

## Step 6: Avvia l'Applicazione Flask

Una volta attivato l'ambiente virtuale, è ora possibile eseguire il server di sviluppo Flask.

```bash
python app.py
```

Questo avvierà il server di sviluppo Flask su `http://localhost:5000`. Dovresti vedere il messaggio:

```
Avviando il server Flask...
```

Ora puoi interagire con i seguenti endpoint:

- **GET `/api/<table_name>`**: Recupera tutti i record da una tabella nel database.
- **POST `/api/<table_name>`**: Inserisce un nuovo record nella tabella del database.

Ad esempio, per recuperare tutti i record dalla tabella `users`, visita:

```
http://localhost:5000/api/users
```

Per inserire un record nella tabella `users`, inviare una richiesta `POST` con dati JSON:

```json
{
  "name": "John Doe",
  "email": "johndoe@example.com"
}
```

## Step 7: Testa l'Applicazione

Puoi testare l'applicazione utilizzando `curl` o un'applicazione client REST come Postman. Ecco alcuni esempi di comandi `curl` per interagire con l'applicazione:

### Ottieni tutti i Dati

```bash
curl http://localhost:5000/api/<table_name>
```

### Inserisci Dati

```bash
curl -X POST http://localhost:5000/api/<table_name> -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "johndoe@example.com"}'
```

## Risoluzione dei Problemi

Se incontri problemi durante la configurazione del progetto Flask, ecco alcune soluzioni comuni:

### Problema 1: Inizializzazione del Database o della Tabella Fallita

Se l'inizializzazione del database fallisce, assicurati che:

- Il database SQLite sia accessibile e scrivibile.
- La tabella specificata esista nel database.

### Problema 2: Le Dipendenze Non si Installano Correttamente

Se `pip` non riesce a installare le dipendenze, provare quanto segue:

- Se `pip` non riesce a installare le dipendenze, prova quanto segue:- Assicurati di utilizzare una versione compatibile di Python (3.7+).
- Upgrade `pip`:

```bash
python -m pip install --upgrade pip
```

- Reinstalla le dipendenze:

```bash
pip install -r requirements.txt
```

## File Structure

Il progetto Flask è strutturato come segue:

```
📦template_flask_project_python
 ┣ 📂config
 ┃ ┗ 📜db_config.py
 ┣ 📂database
 ┃ ┗ 📜example.db
 ┣ 📂models
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┗ 📜model.cpython-310.pyc
 ┃ ┗ 📜model.py
 ┣ 📂routes
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┗ 📜routes.cpython-310.pyc
 ┃ ┗ 📜routes.py
 ┣ 📂test
 ┃ ┗ 📜test.py
 ┣ 📂utils
 ┃ ┗ 📜helpers.py
 ┣ 📜app.py
 ┣ 📜requirements.txt
 ┗ 📜startup.md
```

- `app.py`: Punto di ingresso dell'applicazione Flask.
- `models/model.py`: Definisce il modello del database.
- `routes/routes.py`: Definisce le rotte per l'applicazione Flask.
- `database/example.db`: File del database SQLite.
- `requirements.txt`: Elenco delle librerie Python richieste.

## Conclusion

Hai configurato con successo il progetto Flask! Sentiti libero di estendere la funzionalità, modificare lo schema del database o aggiungere nuove rotte in base alle tue esigenze.

Buon coding!
