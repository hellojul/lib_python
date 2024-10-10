# Fonctions de manipulation de chaînes de caractères

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def capitalize_first_letter(s):
    return s.capitalize()

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_consonants(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def word_count(s):
    return len(s.split())

def is_palindrome(s):
    cleaned = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned == cleaned[::-1]

def char_frequencies(s):
    return {char: s.count(char) for char in set(s)}

def find_substring(s, substring):
    return s.find(substring)

def split_by_delimiter(s, delimiter):
    return s.split(delimiter)

def join_list_to_string(lst, delimiter):
    return delimiter.join(lst)

def remove_punctuation(s):
    import string
    return s.translate(str.maketrans('', '', string.punctuation))

def truncate_string(s, length):
    return s[:length] if len(s) > length else s

def remove_digits(s):
    return ''.join([i for i in s if not i.isdigit()])

def get_all_links(soup):
    return [a['href'] for a in soup.find_all('a', href=True)]

