from datetime import datetime, timedelta, date

# 1. Obtenir la date et l'heure actuelles
def get_current_datetime():
    return datetime.now()

# 2. Obtenir la date actuelle seulement
def get_current_date():
    return date.today()

# 3. Formater une date en chaîne de caractères
def format_date(dt, format_str="%Y-%m-%d %H:%M:%S"):
    return dt.strftime(format_str)

# 4. Convertir une chaîne en objet datetime
def parse_date(date_str, format_str="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(date_str, format_str)

# 5. Ajouter ou soustraire des jours à une date
def add_days_to_date(dt, days):
    return dt + timedelta(days=days)

# 6. Calculer la différence entre deux dates
def get_date_difference(date1, date2):
    return abs((date2 - date1).days)

# 7. Vérifier si une année est bissextile
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# 8. Obtenir le jour de la semaine d'une date (0=Lundi, 6=Dimanche)
def get_weekday(dt):
    return dt.weekday()

# 9. Obtenir le premier et dernier jour du mois
def get_first_day_of_month(dt):
    return dt.replace(day=1)

def get_last_day_of_month(dt):
    next_month = dt.replace(day=28) + timedelta(days=4)  # Passer au mois suivant
    return next_month - timedelta(days=next_month.day)

# 10. Convertir un timestamp en datetime
def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp)

# Exemples d'utilisation
if __name__ == "__main__":
    # Date actuelle
    print("Date actuelle:", get_current_datetime())

    # Formater la date actuelle
    current_date = get_current_datetime()
    print("Date formatée:", format_date(current_date, "%d/%m/%Y"))

    # Convertir une chaîne en date
    date_str = "2024-10-12 14:30:00"
    parsed_date = parse_date(date_str)
    print("Date convertie:", parsed_date)

    # Ajouter 10 jours à la date actuelle
    new_date = add_days_to_date(current_date, 10)
    print("Date après ajout de 10 jours:", new_date)

    # Différence entre deux dates
    date1 = parse_date("2024-10-01 00:00:00")
    date2 = parse_date("2024-10-12 00:00:00")
    diff_days = get_date_difference(date1, date2)
    print("Différence en jours:", diff_days)

    # Vérifier si une année est bissextile
    year = 2024
    print(f"L'année {year} est-elle bissextile?", is_leap_year(year))

    # Obtenir le jour de la semaine
    print("Jour de la semaine:", get_weekday(current_date))

    # Premier et dernier jour du mois
    print("Premier jour du mois:", get_first_day_of_month(current_date))
    print("Dernier jour du mois:", get_last_day_of_month(current_date))

    # Convertir un timestamp en datetime
    timestamp = 1697051400  # Exemple de timestamp
    print("Datetime à partir du timestamp:", timestamp_to_datetime(timestamp))

