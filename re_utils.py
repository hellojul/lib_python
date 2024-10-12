import re

class RegexUtilities:
    # === Fonctions de validation et nettoyage ===

    def is_valid_email(self, email: str) -> bool:
        """
        Checks if the input string is a valid email address.
        """
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))

    def is_valid_password(self, password: str) -> bool:
        """
        Validates a password to ensure it has at least 8 characters,
        one uppercase letter, one lowercase letter, and one digit.
        """
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$'
        return bool(re.match(pattern, password))

    def clean_string(self, input_string: str) -> str:
        """
        Removes all non-alphanumeric characters from the string.
        """
        return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

    def remove_extra_spaces(self, text: str) -> str:
        """
        Removes extra spaces between words in the text.
        """
        return re.sub(r'\s+', ' ', text).strip()

    # === Fonctions d'extraction ===

    def extract_phone_numbers(self, text: str) -> list:
        """
        Extracts all phone numbers from a given text.
        Assumes phone numbers are in the format XXX-XXX-XXXX or (XXX) XXX-XXXX.
        """
        pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        return re.findall(pattern, text)

    def extract_emails(self, text: str) -> list:
        """
        Extracts all email addresses from a given text.
        """
        pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        return re.findall(pattern, text)

    def extract_urls(self, text: str) -> list:
        """
        Extracts all URLs from a given text.
        """
        pattern = r'https?://[^\s]+'
        return re.findall(pattern, text)

    # === Fonctions de recherche et remplacement ===

    def find_capitalized_words(self, text: str) -> list:
        """
        Finds all words in the text that start with a capital letter.
        """
        pattern = r'\b[A-Z][a-z]*\b'
        return re.findall(pattern, text)

    def split_into_words(self, text: str) -> list:
        """
        Splits a string into individual words.
        """
        return re.findall(r'\b\w+\b', text)

    def replace_word(self, text: str, old_word: str, new_word: str) -> str:
        """
        Replaces all occurrences of old_word with new_word in the text.
        """
        return re.sub(rf'\b{old_word}\b', new_word, text)

    def censor_profanity(self, text: str, profanity_list: list) -> str:
        """
        Censors all words in the profanity list by replacing them with '****'.
        """
        for word in profanity_list:
            text = re.sub(rf'\b{word}\b', '****', text, flags=re.IGNORECASE)
        return text

    def find_dates(self, text: str) -> list:
        """
        Finds all dates in the format DD/MM/YYYY or MM/DD/YYYY.
        """
        pattern = r'\b(?:\d{2}[-/]\d{2}[-/]\d{4})\b'
        return re.findall(pattern, text)

    def find_words_with_pattern(self, text: str, pattern: str) -> list:
        """
        Finds all words in the text that match a custom regex pattern.
        """
        return re.findall(pattern, text)

    # === Fonctions de vérification ===

    def contains_pattern(self, text: str, pattern: str) -> bool:
        """
        Checks if the text contains a given regex pattern.
        """
        return bool(re.search(pattern, text))

    def is_valid_ip_address(self, ip_address: str) -> bool:
        """
        Validates if the input string is a valid IPv4 address.
        """
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        return bool(re.match(pattern, ip_address))

    def is_valid_url(self, url: str) -> bool:
        """
        Validates if the input string is a valid URL.
        """
        pattern = r'https?://[^\s/$.?#].[^\s]*'
        return bool(re.match(pattern, url))

