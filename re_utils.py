import re

# Function to check if a string contains a valid email
def is_valid_email(email):
    """
    Checks if the input string is a valid email address.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

# Function to extract all phone numbers from a text
def extract_phone_numbers(text):
    """
    Extracts all phone numbers from a given text.
    Assumes phone numbers are in the format XXX-XXX-XXXX or (XXX) XXX-XXXX.
    """
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

# Function to clean up a string by removing non-alphanumeric characters
def clean_string(input_string):
    """
    Removes all non-alphanumeric characters from the string.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

# Function to find all words in a text that start with a capital letter
def find_capitalized_words(text):
    """
    Finds all words in the text that start with a capital letter.
    """
    pattern = r'\b[A-Z][a-z]*\b'
    return re.findall(pattern, text)

# Function to split a string into words
def split_into_words(text):
    """
    Splits a string into individual words.
    """
    return re.findall(r'\b\w+\b', text)

# Function to validate a password (at least 8 characters, one uppercase, one lowercase, one digit)
def is_valid_password(password):
    """
    Validates a password to ensure it has at least 8 characters,
    one uppercase letter, one lowercase letter, and one digit.
    """
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return bool(re.match(pattern, password))

# Function to remove extra spaces from a string
def remove_extra_spaces(text):
    """
    Removes extra spaces between words in the text.
    """
    return re.sub(r'\s+', ' ', text).strip()

# Function to replace a word in a string
def replace_word(text, old_word, new_word):
    """
    Replaces all occurrences of old_word with new_word in the text.
    """
    return re.sub(rf'\b{old_word}\b', new_word, text)

