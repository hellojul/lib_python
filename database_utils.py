# database_utils.py
# pip install mysql-connector-python

import sqlite3
import mysql.connector
from mysql.connector import Error

# ----------------- SQLite Utilities -----------------

# 1. Function to create a SQLite connection
# Fonction pour créer une connexion à une base de données SQLite
def create_sqlite_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite DB: {db_file}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to SQLite DB: {e}")
        return None

# 2. Function to execute a query (INSERT, UPDATE, DELETE) in SQLite
# Fonction pour exécuter une requête (INSERT, UPDATE, DELETE) dans SQLite
def execute_sqlite_query(conn, query, params=None):
    try:
        cur = conn.cursor()
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        conn.commit()
        print(f"Query executed successfully: {query}")
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")

# 3. Function to fetch data from a SQLite query
# Fonction pour récupérer des données avec une requête SELECT dans SQLite
def fetch_sqlite_data(conn, query, params=None):
    try:
        cur = conn.cursor()
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Error fetching data: {e}")
        return None

# 4. Function to create a table in SQLite
# Fonction pour créer une table dans SQLite
def create_sqlite_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
        print("Table created successfully")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

# ----------------- MySQL Utilities -----------------

# 5. Function to create a MySQL connection
# Fonction pour créer une connexion à une base de données MySQL
def create_mysql_connection(host, user, password, database):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if conn.is_connected():
            print(f"Connected to MySQL DB: {database}")
            return conn
    except Error as e:
        print(f"Error connecting to MySQL DB: {e}")
        return None

# 6. Function to execute a query (INSERT, UPDATE, DELETE) in MySQL
# Fonction pour exécuter une requête (INSERT, UPDATE, DELETE) dans MySQL
def execute_mysql_query(conn, query, params=None):
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        print(f"Query executed successfully: {query}")
    except Error as e:
        print(f"Error executing query: {e}")

# 7. Function to fetch data from a MySQL query
# Fonction pour récupérer des données avec une requête SELECT dans MySQL
def fetch_mysql_data(conn, query, params=None):
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error fetching data: {e}")
        return None

# 8. Function to create a table in MySQL
# Fonction pour créer une table dans MySQL
def create_mysql_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print("Table created successfully")
    except Error as e:
        print(f"Error creating table: {e}")

# ----------------- General Database Utilities -----------------

# 9. Function to close the database connection (SQLite and MySQL)
# Fonction pour fermer une connexion à la base de données (SQLite et MySQL)
def close_connection(conn):
    if conn:
        conn.close()
        print("Connection closed")

# 10. Function to insert multiple rows of data in bulk (SQLite & MySQL)
# Fonction pour insérer plusieurs lignes de données en une fois (SQLite et MySQL)
def insert_multiple_rows(conn, query, data_list):
    try:
        cur = conn.cursor()
        cur.executemany(query, data_list)
        conn.commit()
        print(f"Inserted {cur.rowcount} rows successfully")
    except (sqlite3.Error, Error) as e:
        print(f"Error inserting multiple rows: {e}")

# Example usage of SQLite functions
if __name__ == "__main__":
    # SQLite Example
    sqlite_conn = create_sqlite_connection("example.db")

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    );
    """
    create_sqlite_table(sqlite_conn, create_table_sql)

    # Insert data into SQLite
    insert_query = "INSERT INTO users (name, age, email) VALUES (?, ?, ?)"
    user_data = [
        ("Alice", 25, "alice@example.com"),
        ("Bob", 30, "bob@example.com"),
        ("Charlie", 35, "charlie@example.com")
    ]
    insert_multiple_rows(sqlite_conn, insert_query, user_data)

    # Fetch data from SQLite
    select_query = "SELECT * FROM users"
    users = fetch_sqlite_data(sqlite_conn, select_query)
    print(f"Fetched data: {users}")

    # Close the connection
    close_connection(sqlite_conn)

    # MySQL Example (uncomment to use)
    # mysql_conn = create_mysql_connection("localhost", "root", "password", "test_db")

    # create_table_sql_mysql = """
    # CREATE TABLE IF NOT EXISTS employees (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     name VARCHAR(255) NOT NULL,
    #     salary FLOAT,
    #     department VARCHAR(255)
    # );
    # """
    # create_mysql_table(mysql_conn, create_table_sql_mysql)

    # Close the MySQL connection
    # close_connection(mysql_conn)

