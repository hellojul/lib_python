import os
import json
import csv
import shutil

# === Fichiers texte ===

# Lit un fichier texte entier
def read_text_file(file_path):
    """Lit un fichier texte et retourne son contenu."""
    with open(file_path, 'r') as file:
        return file.read()

# Écrit du texte dans un fichier
def write_text_file(file_path, content):
    """Écrit du texte dans un fichier texte."""
    with open(file_path, 'w') as file:
        file.write(content)

# Effacer le contenue d'un fichier
def clear_file_content(file_path):
    try:
        with open(file_path, 'w') as file:
            pass
    except Exception as e:
        print(f'Error while clearing the file content: {e}')

# Ajoute du texte à la fin d'un fichier texte
def append_text_file(file_path, content):
    """Ajoute du texte à la fin d'un fichier texte."""
    with open(file_path, 'a') as file:
        file.write(content)

# Compte le nombre de lignes dans un fichier texte
def count_lines_in_file(file_path):
    """Compte le nombre de lignes dans un fichier texte."""
    with open(file_path, 'r') as file:
        return len(file.readlines())

# Recherche un mot ou une phrase dans un fichier texte
def find_in_file(file_path, keyword):
    """Recherche un mot ou une phrase dans un fichier texte."""
    with open(file_path, 'r') as file:
        for line in file:
            if keyword in line:
                return True
    return False

# === JSON ===

# Lit un fichier JSON et retourne un dictionnaire
def read_json(file_path):
    """Lit un fichier JSON et retourne un dictionnaire."""
    with open(file_path, 'r') as file:
        return json.load(file)

# Écrit un dictionnaire dans un fichier JSON
def write_json(file_path, data):
    """Écrit un dictionnaire dans un fichier JSON."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Met à jour un fichier JSON avec de nouvelles données
def update_json_file(file_path, new_data):
    """Met à jour un fichier JSON avec de nouvelles données."""
    data = read_json(file_path)
    data.update(new_data)
    write_json(file_path, data)

# === CSV ===

# Lit un fichier CSV et le convertit en liste de dictionnaires
def read_csv(file_path):
    """Lit un fichier CSV et retourne une liste de dictionnaires."""
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Écrit une liste de dictionnaires dans un fichier CSV
def write_csv(file_path, data):
    """Écrit une liste de dictionnaires dans un fichier CSV."""
    if len(data) > 0:
        keys = data[0].keys()
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

# Ajoute une nouvelle ligne de données dans un fichier CSV
def append_to_csv(file_path, new_row):
    """Ajoute une nouvelle ligne dans un fichier CSV."""
    with open(file_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=new_row.keys())
        writer.writerow(new_row)

# === Autres manipulations de fichiers ===

# Liste les fichiers dans un répertoire donné
def list_files_in_directory(directory_path):
    """Liste tous les fichiers dans un répertoire."""
    return os.listdir(directory_path)

# Vérifie si un fichier existe
def file_exists(file_path):
    """Vérifie si un fichier existe."""
    return os.path.isfile(file_path)

# Supprime un fichier
def delete_file(file_path):
    """Supprime un fichier."""
    if file_exists(file_path):
        os.remove(file_path)

# Copie un fichier vers un autre emplacement
def copy_file(src, dest):
    """Copie un fichier d'un emplacement source vers une destination."""
    shutil.copy(src, dest)

# Déplace un fichier vers un autre emplacement
def move_file(src, dest):
    """Déplace un fichier d'un emplacement source vers une destination."""
    shutil.move(src, dest)

# Retourne la taille d'un fichier
def get_file_size(file_path):
    """Retourne la taille d'un fichier en octets."""
    return os.path.getsize(file_path)

