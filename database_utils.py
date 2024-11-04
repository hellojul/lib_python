import sqlite3
from typing import List, Tuple, Any, Optional

# Connexion à la base de données SQLite
def connect(db_name: str) -> sqlite3.Connection:
    """Crée et retourne une connexion à la base de données SQLite."""
    return sqlite3.connect(db_name)

# Création d'une table
def create_table(conn: sqlite3.Connection, table_name: str, columns: str) -> None:
    """
    Crée une table avec le nom et les colonnes spécifiés.
    Exemple de `columns`: "id INTEGER PRIMARY KEY, name TEXT, age INTEGER"
    """
    with conn:
        conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")

# Ajout de colonnes à une table existante
def add_column(conn: sqlite3.Connection, table_name: str, column_definition: str) -> None:
    """
    Ajoute une colonne à une table existante.
    Exemple de `column_definition`: "email TEXT"
    """
    with conn:
        conn.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_definition}")

# Insertion sécurisée de données
def insert_data(conn: sqlite3.Connection, table_name: str, columns: str, values: Tuple[Any]) -> None:
    placeholders = ', '.join('?' * len(values))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    with conn:
        conn.execute(query, values)

# Lecture de toutes les données
def fetch_all(conn: sqlite3.Connection, table_name: str) -> List[Tuple]:
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()

# Récupération de données avec une condition
def fetch_by_condition(conn: sqlite3.Connection, table_name: str, condition: str, params: Tuple) -> List[Tuple]:
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name} WHERE {condition}", params)
    return cursor.fetchall()

# Récupération de colonnes spécifiques
def fetch_columns(conn: sqlite3.Connection, table_name: str, columns: str, condition: Optional[str] = None, params: Optional[Tuple] = ()) -> List[Tuple]:
    """
    Récupère des colonnes spécifiques d'une table avec une condition optionnelle.
    """
    query = f"SELECT {columns} FROM {table_name}"
    if condition:
        query += f" WHERE {condition}"
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()

# Affichage des colonnes d'une table
def list_columns(conn: sqlite3.Connection, table_name: str) -> List[str]:
    """Retourne les noms des colonnes d'une table."""
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    return [col[1] for col in cursor.fetchall()]

# Comptage des lignes selon une condition
def count_rows_with_condition(conn: sqlite3.Connection, table_name: str, condition: str, params: Tuple) -> int:
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {condition}", params)
    return cursor.fetchone()[0]

# Mise à jour de données
def update_data(conn: sqlite3.Connection, table_name: str, updates: str, condition: str, params: Tuple) -> None:
    query = f"UPDATE {table_name} SET {updates} WHERE {condition}"
    with conn:
        conn.execute(query, params)

# Suppression de données
def delete_data(conn: sqlite3.Connection, table_name: str, condition: str, params: Tuple) -> None:
    query = f"DELETE FROM {table_name} WHERE {condition}"
    with conn:
        conn.execute(query, params)

# Analyse de la structure de la base de données
def analyze_database(conn: sqlite3.Connection) -> List[Tuple[str, int]]:
    """
    Retourne la liste des tables dans la base de données avec le nombre de lignes dans chaque table.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    analysis = []
    for table in tables:
        table_name = table[0]
        count = count_rows(conn, table_name)
        analysis.append((table_name, count))
    return analysis

# Récupération des tables de la base de données
def list_tables(conn: sqlite3.Connection) -> List[str]:
    """Retourne une liste des tables dans la base de données."""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    return [table[0] for table in cursor.fetchall()]

# Récupération des valeurs uniques dans une colonne
def fetch_unique_values(conn: sqlite3.Connection, table_name: str, column: str) -> List[Any]:
    """Retourne les valeurs uniques d'une colonne dans une table."""
    cursor = conn.cursor()
    cursor.execute(f"SELECT DISTINCT {column} FROM {table_name}")
    return [row[0] for row in cursor.fetchall()]

# Création d'un index pour une colonne
def create_index(conn: sqlite3.Connection, index_name: str, table_name: str, column: str) -> None:
    """
    Crée un index sur une colonne spécifique pour accélérer les requêtes.
    """
    with conn:
        conn.execute(f"CREATE INDEX IF NOT EXISTS {index_name} ON {table_name} ({column})")

# Suppression d'une table
def drop_table(conn: sqlite3.Connection, table_name: str) -> None:
    """Supprime une table de la base de données."""
    with conn:
        conn.execute(f"DROP TABLE IF EXISTS {table_name}")

# Comptage des lignes dans une table
def count_rows(conn: sqlite3.Connection, table_name: str) -> int:
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    return cursor.fetchone()[0]

# Exécution d'une requête SQL personnalisée
def execute_query(conn: sqlite3.Connection, query: str, params: Optional[Tuple] = ()) -> List[Tuple]:
    """Exécute une requête SQL personnalisée et retourne les résultats."""
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()

# Création d'une table temporaire
def create_temp_table(conn: sqlite3.Connection, table_name: str, columns: str) -> None:
    """
    Crée une table temporaire pour des opérations de test ou intermédiaires.
    """
    with conn:
        conn.execute(f"CREATE TEMP TABLE IF NOT EXISTS {table_name} ({columns})")

# Création d'une vue
def create_view(conn: sqlite3.Connection, view_name: str, query: str) -> None:
    """
    Crée une vue pour une requête spécifique.
    """
    with conn:
        conn.execute(f"CREATE VIEW IF NOT EXISTS {view_name} AS {query}")

# Suppression d'une vue
def drop_view(conn: sqlite3.Connection, view_name: str) -> None:
    """Supprime une vue existante."""
    with conn:
        conn.execute(f"DROP VIEW IF EXISTS {view_name}")

# Fermeture de la connexion à la base de données
def close_connection(conn: sqlite3.Connection) -> None:
    conn.close()

