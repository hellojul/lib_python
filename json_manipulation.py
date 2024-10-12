import json

class JSONManager:
    """
    Classe pour gérer les opérations de lecture, écriture, manipulation, et transformation de fichiers JSON.
    """

    # === Fonctions de lecture et d'écriture JSON ===

    @staticmethod
    def read_json(file):
        """
        Lit un fichier JSON et retourne son contenu sous forme de dictionnaire.
        """
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def write_json(file, data):
        """
        Écrit des données dans un fichier JSON de manière formatée.
        """
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # === Fonctions de manipulation des données JSON ===

    @staticmethod
    def update_json(file, key, new_value):
        """
        Met à jour la valeur d'une clé existante dans un fichier JSON.
        """
        data = JSONManager.read_json(file)
        data[key] = new_value
        JSONManager.write_json(file, data)

    @staticmethod
    def delete_key_json(file, key):
        """
        Supprime une clé spécifique d'un fichier JSON.
        """
        data = JSONManager.read_json(file)
        if key in data:
            del data[key]
        JSONManager.write_json(file, data)

    @staticmethod
    def add_key_json(file, key, value):
        """
        Ajoute une nouvelle clé et valeur dans un fichier JSON.
        """
        data = JSONManager.read_json(file)
        data[key] = value
        JSONManager.write_json(file, data)

    @staticmethod
    def search_key_json(file, key):
        """
        Recherche une clé dans un fichier JSON et retourne sa valeur.
        Si la clé n'existe pas, retourne None.
        """
        data = JSONManager.read_json(file)
        return data.get(key, None)

    @staticmethod
    def key_exists_json(file, key):
        """
        Vérifie si une clé spécifique existe dans un fichier JSON.
        """
        data = JSONManager.read_json(file)
        return key in data

    @staticmethod
    def merge_json(file1, file2, output_file):
        """
        Fusionne deux fichiers JSON et sauvegarde le résultat dans un nouveau fichier.
        """
        data1 = JSONManager.read_json(file1)
        data2 = JSONManager.read_json(file2)
        data1.update(data2)
        JSONManager.write_json(output_file, data1)

    @staticmethod
    def display_json(file):
        """
        Affiche le contenu d'un fichier JSON de manière lisible dans la console.
        """
        data = JSONManager.read_json(file)
        print(json.dumps(data, ensure_ascii=False, indent=4))

    # === Fonctions supplémentaires pour manipulation avancée du JSON ===

    @staticmethod
    def extract_all_keys(file):
        """
        Extrait et retourne une liste de toutes les clés présentes dans un fichier JSON.
        """
        data = JSONManager.read_json(file)
        return list(data.keys())

    @staticmethod
    def invert_json(file):
        """
        Inverse les clés et les valeurs dans un fichier JSON si les valeurs sont hashables (par exemple, des chaînes de caractères).
        """
        data = JSONManager.read_json(file)
        inverted_data = {v: k for k, v in data.items() if isinstance(v, (str, int, float))}
        JSONManager.write_json(file, inverted_data)

    @staticmethod
    def filter_json(file, condition):
        """
        Filtre les paires clé-valeur d'un fichier JSON selon une condition donnée (fonction lambda).
        """
        data = JSONManager.read_json(file)
        filtered_data = {k: v for k, v in data.items() if condition(k, v)}
        return filtered_data

    @staticmethod
    def dict_to_json_string(data):
        """
        Convertit un dictionnaire Python en une chaîne JSON.
        """
        return json.dumps(data, ensure_ascii=False, indent=4)

    @staticmethod
    def json_string_to_dict(json_string):
        """
        Convertit une chaîne JSON en un dictionnaire Python.
        """
        return json.loads(json_string)

    @staticmethod
    def merge_json_dicts(dict1, dict2):
        """
        Fusionne deux dictionnaires JSON en un seul.
        """
        dict1.update(dict2)
        return dict1

    @staticmethod
    def sort_json_by_key(file):
        """
        Trie les paires clé-valeur d'un fichier JSON par clé de manière ascendante.
        """
        data = JSONManager.read_json(file)
        sorted_data = dict(sorted(data.items()))
        JSONManager.write_json(file, sorted_data)

    @staticmethod
    def search_key_recursive(data, target_key):
        """
        Recherche une clé dans un dictionnaire JSON de manière récursive, incluant les structures imbriquées.
        """
        if isinstance(data, dict):
            if target_key in data:
                return data[target_key]
            for key, value in data.items():
                result = JSONManager.search_key_recursive(value, target_key)
                if result:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = JSONManager.search_key_recursive(item, target_key)
                if result:
                    return result
        return None

    # === Nouvelles fonctions utiles ajoutées ===

    @staticmethod
    def remove_null_values(file):
        """
        Supprime toutes les paires clé-valeur avec des valeurs nulles dans un fichier JSON.
        """
        data = JSONManager.read_json(file)
        cleaned_data = {k: v for k, v in data.items() if v is not None}
        JSONManager.write_json(file, cleaned_data)

    @staticmethod
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

    @staticmethod
    def convert_keys_to_uppercase(file):
        """
        Convertit toutes les clés d'un fichier JSON en majuscules.
        """
        data = JSONManager.read_json(file)
        uppercased_data = {k.upper(): v for k, v in data.items()}
        JSONManager.write_json(file, uppercased_data)

    @staticmethod
    def split_json_by_key(file, key, output_file_true, output_file_false):
        """
        Divise un fichier JSON en deux fichiers selon la présence d'une clé.
        """
        data = JSONManager.read_json(file)
        true_data = {k: v for k, v in data.items() if key in v}
        false_data = {k: v for k, v in data.items() if key not in v}
        JSONManager.write_json(output_file_true, true_data)
        JSONManager.write_json(output_file_false, false_data)

    @staticmethod
    def rename_json_key(file, old_key, new_key):
        """
        Renomme une clé spécifique dans un fichier JSON.
        """
        data = JSONManager.read_json(file)
        if old_key in data:
            data[new_key] = data.pop(old_key)
        JSONManager.write_json(file, data)

