import os
import shutil
from datetime import datetime

# === Fonctions pour la manipulation de répertoires ===

# Retourne le répertoire de travail actuel
def get_current_directory():
    return os.getcwd()

# Change le répertoire de travail vers le chemin spécifié
def change_directory(path):
    os.chdir(path)

# Liste tous les fichiers et répertoires dans le chemin spécifié
def list_directory_contents(path="."):
    return os.listdir(path)

# Crée un répertoire au chemin spécifié
def create_directory(path):
    os.mkdir(path)

# Supprime un répertoire vide au chemin spécifié
def remove_directory(path):
    os.rmdir(path)

# Crée des répertoires imbriqués
def create_nested_directories(path):
    os.makedirs(path)

# Supprime un répertoire, même s'il contient des sous-dossiers et fichiers
def remove_nested_directories(path):
    shutil.rmtree(path)

# === Fonctions pour la manipulation de fichiers ===

# Crée un fichier vide
def create_empty_file(path):
    with open(path, 'w') as file:
        pass  # Crée un fichier vide

# Supprime un fichier
def remove_file(path):
    os.remove(path)

# Renomme un fichier ou un répertoire
def rename_file_or_directory(old_path, new_path):
    os.rename(old_path, new_path)

# Copie un fichier d'une destination à une autre
def copy_file(source, destination):
    shutil.copy2(source, destination)

# Déplace un fichier d'une destination à une autre
def move_file(source, destination):
    shutil.move(source, destination)

# === Fonctions d'information sur les fichiers et répertoires ===

# Retourne la taille d'un fichier
def get_file_size(path):
    return os.path.getsize(path)

# Retourne l'extension d'un fichier
def get_file_extension(path):
    return os.path.splitext(path)[1]

# Retourne la dernière date de modification d'un fichier
def get_last_modified_time(path):
    timestamp = os.path.getmtime(path)
    return datetime.fromtimestamp(timestamp)

# Vérifie si le chemin spécifié est un fichier
def is_file(path):
    return os.path.isfile(path)

# Vérifie si le chemin spécifié est un répertoire
def is_directory(path):
    return os.path.isdir(path)

# Vérifie si un fichier existe
def file_exists(path):
    return os.path.exists(path)

# Vérifie si un répertoire existe
def directory_exists(path):
    return os.path.isdir(path)

# === Fonctions sur les chemins de fichiers ===

# Retourne le chemin absolu pour un chemin donné
def get_absolute_path(path):
    return os.path.abspath(path)

# Concatène plusieurs chemins
def join_paths(*paths):
    return os.path.join(*paths)

# Sépare un chemin en répertoire et fichier
def split_path(path):
    return os.path.split(path)

# Retourne le nom de fichier ou le dernier répertoire
def get_basename(path):
    return os.path.basename(path)

# Retourne le répertoire parent
def get_dirname(path):
    return os.path.dirname(path)

# === Informations sur l'environnement système ===

# Retourne la valeur d'une variable d'environnement
def get_environment_variable(var):
    return os.getenv(var)

# Définit une variable d'environnement
def set_environment_variable(var, value):
    os.environ[var] = value

# Retourne le répertoire "home" de l'utilisateur actuel
def get_user_home_directory():
    return os.path.expanduser("~")

# Retourne le répertoire temporaire utilisé par le système
def get_temp_directory():
    return os.path.gettempdir()

# Retourne le nom de la plateforme
def get_platform_name():
    return os.name

