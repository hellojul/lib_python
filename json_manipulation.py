import json

# Fonction pour lire un fichier JSON et retourner ses données sous forme de dictionnaire

def read_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

# Fonction pour écrire des données dans un fichier JSON
def write_json(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Fonction pour mettre à jour une clé existante dans un fichier JSON
def update_json(file, key, new_value):
    data = read_json(file)
    data[key] = new_value
    write_json(file, data)

# Fonction pour supprimer une clé spécifique d'un fichier JSON
def delete_key_json(file, key):
    data = read_json(file)
    if key in data:
        del data[key]
    write_json(file, data)

# Fonction pour ajouter une nouvelle clé et valeur dans un fichier JSON
def add_key_json(file, key, value):
    data = read_json(file)
    data[key] = value
    write_json(file, data)

# Fonction pour rechercher une clé dans un fichier JSON et retourner sa valeur
def search_key_json(file, key):
    data = read_json(file)
    return data.get(key, None)

# Fonction pour vérifier si une clé spécifique existe dans le fichier JSON
def key_exists_json(file, key):
    data = read_json(file)
    return key in data

# Fonction pour fusionner deux fichiers JSON en un seul
def merge_json(file1, file2, output_file):
    data1 = read_json(file1)
    data2 = read_json(file2)
    data1.update(data2)
    write_json(output_file, data1)

# Fonction pour afficher les données JSON dans un format lisible
def display_json(file):
    data = read_json(file)
    print(json.dumps(data, ensure_ascii=False, indent=4))


