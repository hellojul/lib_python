import re

# === Fonctions de validation et nettoyage ===

def is_valid_email(self, email: str) -> bool:
    """
    Vérifie si la chaîne d'entrée est une adresse e-mail valide.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def is_valid_password(self, password: str) -> bool:
    """
    Valide un mot de passe pour s'assurer qu'il contient au moins 8 caractères,
    une lettre majuscule, une lettre minuscule, et un chiffre.
    """
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return bool(re.match(pattern, password))

def clean_string(self, input_string: str) -> str:
    """
    Supprime tous les caractères non alphanumériques de la chaîne.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

def remove_extra_spaces(self, text: str) -> str:
    """
    Supprime les espaces supplémentaires entre les mots dans le texte.
    """
    return re.sub(r'\s+', ' ', text).strip()

# === Fonctions d'extraction ===

def extract_phone_numbers(self, text: str) -> list:
    """
    Extrait tous les numéros de téléphone d'un texte donné.
    Suppose que les numéros sont au format XXX-XXX-XXXX ou (XXX) XXX-XXXX.
    """
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

def extract_emails(self, text: str) -> list:
    """
    Extrait toutes les adresses e-mail d'un texte donné.
    """
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

def extract_urls(self, text: str) -> list:
    """
    Extrait tous les URL d'un texte donné.
    """
    pattern = r'https?://[^\s]+'
    return re.findall(pattern, text)

# === Fonctions de recherche et remplacement ===

def find_capitalized_words(self, text: str) -> list:
    """
    Trouve tous les mots dans le texte qui commencent par une majuscule.
    """
    pattern = r'\b[A-Z][a-z]*\b'
    return re.findall(pattern, text)

def split_into_words(self, text: str) -> list:
    """
    Divise une chaîne en mots individuels.
    """
    return re.findall(r'\b\w+\b', text)

def replace_word(self, text: str, old_word: str, new_word: str) -> str:
    """
    Remplace toutes les occurrences de old_word par new_word dans le texte.
    """
    return re.sub(rf'\b{old_word}\b', new_word, text)

def censor_profanity(self, text: str, profanity_list: list) -> str:
    """
    Censure tous les mots dans la liste de vulgarités en les remplaçant par '****'.
    """
    for word in profanity_list:
        text = re.sub(rf'\b{word}\b', '****', text, flags=re.IGNORECASE)
    return text

def find_dates(self, text: str) -> list:
    """
    Trouve toutes les dates au format JJ/MM/AAAA ou MM/JJ/AAAA.
    """
    pattern = r'\b(?:\d{2}[-/]\d{2}[-/]\d{4})\b'
    return re.findall(pattern, text)

def find_words_with_pattern(self, text: str, pattern: str) -> list:
    """
    Trouve tous les mots dans le texte qui correspondent à un motif regex personnalisé.
    """
    return re.findall(pattern, text)

# === Fonctions de vérification ===

def contains_pattern(self, text: str, pattern: str) -> bool:
    """
    Vérifie si le texte contient un motif regex donné.
    """
    return bool(re.search(pattern, text))

def is_valid_ip_address(self, ip_address: str) -> bool:
    """
    Vérifie si la chaîne d'entrée est une adresse IPv4 valide.
    """
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return bool(re.match(pattern, ip_address))

def is_valid_url(self, url: str) -> bool:
    """
    Vérifie si la chaîne d'entrée est une URL valide.
    """
    pattern = r'https?://[^\s/$.?#].[^\s]*'
    return bool(re.match(pattern, url))

