import string

def to_uppercase(s):
    """Convertit la chaîne d'entrée en majuscules."""
    return s.upper()

def to_lowercase(s):
    """Convertit la chaîne d'entrée en minuscules."""
    return s.lower()

def capitalize_first_letter(s):
    """Met en majuscule la première lettre de la chaîne d'entrée."""
    return s.capitalize()

def reverse_string(s):
    """Inverse la chaîne d'entrée."""
    return s[::-1]

def count_vowels(s):
    """Compte le nombre de voyelles dans la chaîne d'entrée."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_consonants(s):
    """Compte le nombre de consonnes dans la chaîne d'entrée."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def word_count(s):
    """Renvoie le nombre de mots dans la chaîne d'entrée."""
    return len(s.split())

def is_palindrome(s):
    """Vérifie si la chaîne d'entrée est un palindrome (en ignorant la casse et les caractères non alphanumériques)."""
    cleaned = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned == cleaned[::-1]

def char_frequencies(s):
    """Renvoie un dictionnaire des fréquences de caractères dans la chaîne d'entrée."""
    return {char: s.count(char) for char in set(s)}

def find_substring(s, substring):
    """Trouve la première occurrence d'une sous-chaîne dans la chaîne d'entrée."""
    return s.find(substring)

def split_by_delimiter(s, delimiter):
    """Divise la chaîne d'entrée par le délimiteur donné."""
    return s.split(delimiter)

def join_list_to_string(lst, delimiter):
    """Joint une liste de chaînes en une seule chaîne, en utilisant le délimiteur spécifié."""
    return delimiter.join(lst)

def remove_punctuation(s):
    """Supprime tous les caractères de ponctuation de la chaîne d'entrée."""
    return s.translate(str.maketrans('', '', string.punctuation))

def truncate_string(s, length):
    """Tronque la chaîne d'entrée à la longueur spécifiée."""
    return s[:length] if len(s) > length else s

def remove_digits(s):
    """Supprime tous les caractères numériques de la chaîne d'entrée."""
    return ''.join([i for i in s if not i.isdigit()])

def get_all_links(soup):
    """Extrait tous les liens 'href' d'un objet soup HTML."""
    return [a['href'] for a in soup.find_all('a', href=True)]

