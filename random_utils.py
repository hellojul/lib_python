import random
import string
from datetime import datetime, timedelta

# 1. Fonction pour générer un entier aléatoire entre deux valeurs
def random_int(min_val, max_val):
    return random.randint(min_val, max_val)

# 2. Fonction pour générer un flottant aléatoire entre deux valeurs
def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)

# 3. Fonction pour choisir un élément aléatoire dans une liste
def random_choice(choices):
    return random.choice(choices)

# 4. Fonction pour mélanger aléatoirement une liste
def shuffle_list(input_list):
    random.shuffle(input_list)
    return input_list

# 5. Fonction pour générer un mot de passe aléatoire
def generate_password(length=8, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# 6. Fonction pour générer une date aléatoire entre deux dates
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# 7. Fonction pour générer une valeur booléenne aléatoire
def random_bool():
    return random.choice([True, False])

# 8. Fonction pour générer une chaîne aléatoire d'une longueur donnée
def random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# 9. Fonction pour générer une liste d'entiers uniques aléatoires
def unique_random_integers(count, min_val, max_val):
    return random.sample(range(min_val, max_val + 1), count)

# 10. Fonction pour simuler un lancer de dé avec un nombre de faces donné
def roll_dice(sides=6):
    return random.randint(1, sides)

# 11. Fonction pour sélectionner n éléments aléatoires dans une liste
def random_sample(input_list, n):
    return random.sample(input_list, n)

# 12. Fonction pour générer une adresse IP aléatoire
def random_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

# 13. Fonction pour lancer une pièce (pile ou face)
def flip_coin():
    return random.choice(["Pile", "Face"])

# 14. Fonction pour générer un code couleur hexadécimal aléatoire
def random_hex_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# 15. Fonction pour générer des coordonnées aléatoires (latitude, longitude)
def random_coordinates():
    latitude = random.uniform(-90.0, 90.0)
    longitude = random.uniform(-180.0, 180.0)
    return latitude, longitude

# 16. Fonction pour simuler des numéros de loterie aléatoires
def random_lottery_numbers(num_numbers=6, min_val=1, max_val=49):
    return random.sample(range(min_val, max_val + 1), num_numbers)

