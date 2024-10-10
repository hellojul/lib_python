import json
import csv
import time
from datetime import datetime
import math

# === Fonctions de manipulation de fichiers et données ===

# Lit le contenu d'un fichier texte
def read_file(file_path):
    """Lit un fichier et retourne son contenu"""
    with open(file_path, 'r') as file:
        return file.read()

# Écrit du texte dans un fichier
def write_file(file_path, content):
    """Écrit du texte dans un fichier"""
    with open(file_path, 'w') as file:
        file.write(content)

# Convertit un fichier JSON en dictionnaire
def json_to_dict(file_path):
    """Lit un fichier JSON et le convertit en dictionnaire"""
    with open(file_path, 'r') as file:
        return json.load(file)

# Écrit un dictionnaire dans un fichier JSON
def dict_to_json(file_path, data):
    """Écrit un dictionnaire dans un fichier JSON"""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Convertit un fichier CSV en liste de dictionnaires
def csv_to_list(file_path):
    """Convertit un fichier CSV en liste de dictionnaires"""
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Écrit une liste de dictionnaires dans un fichier CSV
def list_to_csv(file_path, data):
    """Écrit une liste de dictionnaires dans un fichier CSV"""
    if len(data) > 0:
        keys = data[0].keys()
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

# === Fonctions de manipulation de chaînes ===

# Met en majuscule la première lettre de chaque mot dans une chaîne
def capitalize_words(s):
    """Met en majuscule la première lettre de chaque mot"""
    return s.title()

# Vérifie si une chaîne est un palindrome
def is_palindrome(s):
    """Vérifie si une chaîne est un palindrome"""
    return s == s[::-1]

# Supprime les espaces dans une chaîne
def remove_whitespace(s):
    """Supprime les espaces dans une chaîne"""
    return s.replace(' ', '')

# === Fonctions mathématiques et traitement des nombres ===

# Vérifie si un nombre est pair
def is_even(n):
    """Retourne True si le nombre est pair"""
    return n % 2 == 0

# Vérifie si un nombre est impair
def is_odd(n):
    """Retourne True si le nombre est impair"""
    return n % 2 != 0

# Retourne la somme des éléments d'une liste
def sum_of_list(lst):
    """Calcule la somme des éléments d'une liste"""
    return sum(lst)

# Calcule la moyenne d'une liste de nombres
def average_of_list(lst):
    """Calcule la moyenne des éléments d'une liste"""
    return sum(lst) / len(lst) if lst else 0

# Calcule l'écart-type d'une liste de nombres
def standard_deviation(lst):
    """Calcule l'écart-type d'une liste de nombres"""
    mean = average_of_list(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return math.sqrt(variance)

# === Fonctions diverses ===

# Aplatie une liste de listes
def flatten_list(lst):
    """Aplatie une liste de listes"""
    return [item for sublist in lst for item in sublist]

# Divise une liste en morceaux de taille fixe
def chunk_list(lst, chunk_size):
    """Divise une liste en sous-listes de taille fixe"""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

# Trouve les doublons dans une liste
def find_duplicates(lst):
    """Retourne une liste des doublons trouvés"""
    return list(set([x for x in lst if lst.count(x) > 1]))

# Trie un dictionnaire par ses valeurs
def sort_dict_by_value(d):
    """Retourne un dictionnaire trié par valeurs"""
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Retourne la date et l'heure actuelles
def get_current_datetime():
    """Retourne la date et l'heure actuelles"""
    return datetime.now()

# Mesure le temps d'exécution d'une fonction
def time_function_execution(func, *args, **kwargs):
    """Mesure le temps d'exécution d'une fonction"""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Temps d'exécution: {execution_time:.4f} secondes")
    return result
