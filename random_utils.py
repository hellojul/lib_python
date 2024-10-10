# random_utils.py

import random
import string
from datetime import datetime, timedelta

# 1. Function to generate a random integer between two values
def random_int(min_val, max_val):
    return random.randint(min_val, max_val)

# 2. Function to generate a random float between two values
def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)

# 3. Function to generate a random choice from a list
def random_choice(choices):
    return random.choice(choices)

# 4. Function to shuffle a list randomly
def shuffle_list(input_list):
    random.shuffle(input_list)
    return input_list

# 5. Function to generate a random password
def generate_password(length=8, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# 6. Function to generate a random date between two dates
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# 7. Function to generate a random boolean value
def random_bool():
    return random.choice([True, False])

# 8. Function to generate a random string of a given length
def random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# 9. Function to generate a list of unique random integers
def unique_random_integers(count, min_val, max_val):
    return random.sample(range(min_val, max_val + 1), count)

# 10. Function to simulate rolling a dice with a given number of sides
def roll_dice(sides=6):
    return random.randint(1, sides)

# 11. Function to pick n random elements from a list
def random_sample(input_list, n):
    return random.sample(input_list, n)

# 12. Function to generate a random IP address
def random_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

# 13. Function to flip a coin (heads or tails)
def flip_coin():
    return random.choice(["Heads", "Tails"])

# 14. Function to generate a random hexadecimal color code
def random_hex_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# 15. Function to generate random coordinates (latitude, longitude)
def random_coordinates():
    latitude = random.uniform(-90.0, 90.0)
    longitude = random.uniform(-180.0, 180.0)
    return latitude, longitude

# 16. Function to simulate a random lottery number
def random_lottery_numbers(num_numbers=6, min_val=1, max_val=49):
    return random.sample(range(min_val, max_val + 1), num_numbers)


