import json

# === Fonctions de lecture et d'écriture JSON ===

def read_json(file):
    """
    Lit un fichier JSON et retourne son contenu sous forme de dictionnaire.
    """
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(file, data):
    """
    Écrit des données dans un fichier JSON de manière formatée.
    """
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# === Fonctions de manipulation des données JSON ===

def update_json(file, key, new_value):
    """
    Met à jour la valeur d'une clé existante dans un fichier JSON.
    """
    data = read_json(file)
    data[key] = new_value
    write_json(file, data)

def delete_key_json(file, key):
    """
    Supprime une clé spécifique d'un fichier JSON.
    """
    data = read_json(file)
    if key in data:
        del data[key]
    write_json(file, data)

def add_key_json(file, key, value):
    """
    Ajoute une nouvelle clé et valeur dans un fichier JSON.
    """
    data = read_json(file)
    data[key] = value
    write_json(file, data)

def search_key_json(file, key):
    """
    Recherche une clé dans un fichier JSON et retourne sa valeur.
    Si la clé n'existe pas, retourne None.
    """
    data = read_json(file)
    return data.get(key, None)

def key_exists_json(file, key):
    """
    Vérifie si une clé spécifique existe dans un fichier JSON.
    """
    data = read_json(file)
    return key in data

def merge_json(file1, file2, output_file):
    """
    Fusionne deux fichiers JSON et sauvegarde le résultat dans un nouveau fichier.
    """
    data1 = read_json(file1)
    data2 = read_json(file2)
    data1.update(data2)
    write_json(output_file, data1)

def display_json(file):
    """
    Affiche le contenu d'un fichier JSON de manière lisible dans la console.
    """
    data = read_json(file)
    print(json.dumps(data, ensure_ascii=False, indent=4))

# === Fonctions supplémentaires pour manipulation avancée du JSON ===

def extract_all_keys(file):
    """
    Extrait et retourne une liste de toutes les clés présentes dans un fichier JSON.
    """
    data = read_json(file)
    return list(data.keys())

def invert_json(file):
    """
    Inverse les clés et les valeurs dans un fichier JSON si les valeurs sont hashables (par exemple, des chaînes de caractères).
    """
    data = read_json(file)
    inverted_data = {v: k for k, v in data.items() if isinstance(v, (str, int, float))}
    write_json(file, inverted_data)

def filter_json(file, condition):
    """
    Filtre les paires clé-valeur d'un fichier JSON selon une condition donnée (fonction lambda).
    """
    data = read_json(file)
    filtered_data = {k: v for k, v in data.items() if condition(k, v)}
    return filtered_data

def dict_to_json_string(data):
    """
    Convertit un dictionnaire Python en une chaîne JSON.
    """
    return json.dumps(data, ensure_ascii=False, indent=4)

def json_string_to_dict(json_string):
    """
    Convertit une chaîne JSON en un dictionnaire Python.
    """
    return json.loads(json_string)

def merge_json_dicts(dict1, dict2):
    """
    Fusionne deux dictionnaires JSON en un seul.
    """
    dict1.update(dict2)
    return dict1

def sort_json_by_key(file):
    """
    Trie les paires clé-valeur d'un fichier JSON par clé de manière ascendante.
    """
    data = read_json(file)
    sorted_data = dict(sorted(data.items()))
    write_json(file, sorted_data)

def search_key_recursive(data, target_key):
    """
    Recherche une clé dans un dictionnaire JSON de manière récursive, incluant les structures imbriquées.
    """
    if isinstance(data, dict):
        if target_key in data:
            return data[target_key]
        for key, value in data.items():
            result = search_key_recursive(value, target_key)
            if result:
                return result
    elif isinstance(data, list):
        for item in data:
            result = search_key_recursive(item, target_key)
            if result:
                return result
    return None

# === Nouvelles fonctions utiles ajoutées ===

def remove_null_values(file):
    """
    Supprime toutes les paires clé-valeur avec des valeurs nulles dans un fichier JSON.
    """
    data = read_json(file)
    cleaned_data = {k: v for k, v in data.items() if v is not None}
    write_json(file, cleaned_data)

def flatten_json(nested_json):
    """
    Aplatie un dictionnaire JSON imbriqué en un dictionnaire à un seul niveau.
    """
    def flatten(d, parent_key='', sep='_'):
        items = []
        for k, v in d.items():
            new_key = f'{parent_key}{sep}{k}' if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    return flatten(nested_json)

def convert_keys_to_uppercase(file):
    """
    Convertit toutes les clés d'un fichier JSON en majuscules.
    """
    data = read_json(file)
    uppercased_data = {k.upper(): v for k, v in data.items()}
    write_json(file, uppercased_data)

def split_json_by_key(file, key, output_file_true, output_file_false):
    """
    Divise un fichier JSON en deux fichiers selon la présence d'une clé.
    """
    data = read_json(file)
    true_data = {k: v for k, v in data.items() if key in v}
    false_data = {k: v for k, v in data.items() if key not in v}
    write_json(output_file_true, true_data)
    write_json(output_file_false, false_data)

def rename_json_key(file, old_key, new_key):
    """
    Renomme une clé spécifique dans un fichier JSON.
    """
    data = read_json(file)
    if old_key in data:
        data[new_key] = data.pop(old_key)
    write_json(file, data)

