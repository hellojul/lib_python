# === Fonctions pour les tuples ===

# Crée un tuple à partir des arguments fournis
def create_tuple(*args):
    return tuple(args)

# Accède à l'élément d'un tuple à un index donné
def access_element(t, index):
    return t[index]

# Retourne la longueur d’un tuple
def tuple_length(t):
    return len(t)

# Concatène deux tuples
def concatenate_tuples(t1, t2):
    return t1 + t2

# Répète un tuple n fois
def repeat_tuple(t, n):
    return t * n

# Compte combien de fois un élément apparaît dans un tuple
def count_item_in_tuple(t, item):
    return t.count(item)

# Inverse l’ordre des éléments dans un tuple
def reverse_tuple(t):
    return t[::-1]

# Retourne l’élément maximum dans un tuple
def max_in_tuple(t):
    return max(t)

# Retourne l’élément minimum dans un tuple
def min_in_tuple(t):
    return min(t)


# === Fonctions pour les dictionnaires ===

# Crée un dictionnaire à partir de listes de clés et de valeurs
def create_dict(keys, values):
    return dict(zip(keys, values))

# Accède à une valeur dans un dictionnaire à partir d’une clé donnée
def access_value(d, key):
    return d.get(key, "Clé non trouvée")

# Met à jour la valeur associée à une clé dans un dictionnaire
def update_value(d, key, value):
    d[key] = value

# Ajoute un nouvel élément au dictionnaire
def add_item_to_dict(d, key, value):
    d[key] = value

# Supprime un élément du dictionnaire selon la clé
def remove_item_from_dict(d, key):
    if key in d:
        del d[key]

# Retourne toutes les clés d’un dictionnaire
def get_dict_keys(d):
    return list(d.keys())

# Retourne toutes les valeurs d’un dictionnaire
def get_dict_values(d):
    return list(d.values())

# Retourne toutes les paires clé-valeur d’un dictionnaire
def get_dict_items(d):
    return list(d.items())

# Fusionne deux dictionnaires
def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

# Inverse les clés et les valeurs dans un dictionnaire
def invert_dict(d):
    return {v: k for k, v in d.items()}

# Trie un dictionnaire selon ses clés
def sort_dict_by_keys(d):
    return dict(sorted(d.items()))

# Trie un dictionnaire selon ses valeurs
def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Retourne la valeur maximale dans un dictionnaire
def get_max_value(d):
    return max(d.values())

# Retourne la valeur minimale dans un dictionnaire
def get_min_value(d):
    return min(d.values())

