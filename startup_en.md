# Flask Project Setup

This is a template for a Flask-based web application with SQLite as the database. This guide will walk you through the process of setting up the project, installing dependencies, and running the application.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Python 3.7+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

## Step 1: Clone the Repository

First, clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/template_flask_project_python.git
cd template_flask_project_python
```

## Step 2: Create a Virtual Environment

A virtual environment isolates your project dependencies from your global Python environment. It's a good practice to create one for each project.

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

- **Windows:**

```bash
venv\Scriptsctivate
```

- **macOS/Linux:**

```bash
source venv/bin/activate
```

Once the virtual environment is activated, your terminal should show `(venv)` before the prompt.

## Step 4: Install Dependencies

Install the required Python libraries using the `pip` command. Make sure your virtual environment is activated when you do this.

```bash
pip install -r requirements.txt
```

This will install the following libraries (and their dependencies):

- `Flask`: Web framework for Python.
- `Flask-CORS`: Handle Cross-Origin Resource Sharing (CORS).
- `SQLite3`: Embedded database for Python.

## Step 5: Database Setup

The project uses SQLite as the database. The database is automatically initialized when the application is first run.

If you want to manually initialize the database, you can use the provided method in the `app.py` file:

```python
initialize_database()
```

This will create a table called `table_name` in the SQLite database file `database/example.db`.

## Step 6: Run the Application

With the virtual environment activated, you can now run the Flask development server.

```bash
python app.py
```

This will start the Flask development server at `http://localhost:5000`. You should see the message:

```
Avviando il server Flask...
```

You can now interact with the following endpoints:

- **GET `/api/<table_name>`**: Fetch all records from a table in the database.
- **POST `/api/<table_name>`**: Insert data into a table in the database. The request body should be a JSON object containing the column names and values.

For example, to fetch all records from a table called `users`, you can visit:

```
http://localhost:5000/api/users
```

To insert a record into the `users` table, send a `POST` request with JSON data:

```json
{
  "name": "John Doe",
  "email": "johndoe@example.com"
}
```

## Step 7: Test the Application

You can test the application using tools like **Postman** or **curl**. Here are some example commands:

### Get All Records

```bash
curl http://localhost:5000/api/<table_name>
```

### Insert Data

```bash
curl -X POST http://localhost:5000/api/<table_name> -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "johndoe@example.com"}'
```

## Troubleshooting

If you encounter any issues with the setup, please refer to the following:

### Issue 1: Database Initialization Fails

If the database or table initialization fails, ensure that:

- The `database/example.db` file is writable by your application.
- The table structure is correctly defined in `app.py` or the model file.

### Issue 2: Dependencies Fail to Install

If `pip` fails to install the dependencies, try the following:

- Ensure you are using a compatible version of Python (3.7+).
- Upgrade `pip`:

```bash
python -m pip install --upgrade pip
```

- Reinstall dependencies:

```bash
pip install -r requirements.txt
```

## File Structure

The project is organized as follows:

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

- `app.py`: Main entry point for the Flask app.
- `models/model.py`: Contains the database logic (CRUD operations).
- `routes/routes.py`: Defines the routes for the Flask app.
- `database/example.db`: The SQLite database file.
- `requirements.txt`: List of required dependencies.

## Conclusion

You have successfully set up the Flask project! Feel free to extend the functionality, modify the database schema, or add new routes according to your needs.

Happy coding!
