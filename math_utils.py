import math

# Calculer le pourcentage d'une valeur
def percentage(part, total):
    if total == 0:
        return 0
    return (part / total) * 100

# Calculer la moyenne d'une liste de nombres
def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Calculer la médiane d'une liste de nombres
def median(numbers):
    n = len(numbers)
    sorted_list = sorted(numbers)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]

# Calculer la factorielle d'un nombre
def factorial(n):
    return math.factorial(n)

# Conversion de degrés en radians
def degrees_to_radians(degrees):
    return math.radians(degrees)

# Conversion de radians en degrés
def radians_to_degrees(radians):
    return math.degrees(radians)

# Calculer le périmètre d'un cercle
def circle_perimeter(radius):
    return 2 * math.pi * radius

# Calculer l'aire d'un cercle
def circle_area(radius):
    return math.pi * (radius ** 2)

# Calculer l'hypoténuse d'un triangle rectangle
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

# Arrondir un nombre à n décimales
def round_to_n_decimal(number, n):
    return round(number, n)

# Générer un nombre aléatoire entre deux valeurs
def random_number(min_value, max_value):
    return random.randint(min_value, max_value)

# Calculer la distance entre deux points dans un plan 2D
def distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculer la pente d'une droite entre deux points
def slope(x1, y1, x2, y2):
    if x2 == x1:
        return None  # Evite la division par zéro
    return (y2 - y1) / (x2 - x1)

# Calculer le montant après l'application d'une remise
def discounted_price(price, discount_rate):
    return price * (1 - discount_rate / 100)

# Calculer les intérêts composés
def compound_interest(principal, rate, time, n=1):
    return principal * (1 + rate / (100 * n))**(n * time)

# Vérifier si un nombre est un nombre premier
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Calculer le PGCD de deux nombres
def gcd(a, b):
    return math.gcd(a, b)

# Calculer le PPCM de deux nombres
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b) if a and b else 0

# Conversion de pourcentage en fraction
def percentage_to_fraction(percentage):
    from fractions import Fraction
    return Fraction(percentage, 100).limit_denominator()

# Conversion de fraction en pourcentage
def fraction_to_percentage(numerator, denominator):
    if denominator == 0:
        return None
    return (numerator / denominator) * 100

# Calculer la somme des carrés d'une liste de nombres
def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

# Calculer la distance Euclidienne dans un espace 3D
def distance_3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

