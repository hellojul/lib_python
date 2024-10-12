import string

class StringManipulator:
    """A class for performing various string manipulations."""

    def to_uppercase(self, s):
        """Converts the input string to uppercase."""
        return s.upper()

    def to_lowercase(self, s):
        """Converts the input string to lowercase."""
        return s.lower()

    def capitalize_first_letter(self, s):
        """Capitalizes the first letter of the input string."""
        return s.capitalize()

    def reverse_string(self, s):
        """Reverses the input string."""
        return s[::-1]

    def count_vowels(self, s):
        """Counts the number of vowels in the input string."""
        vowels = "aeiouAEIOU"
        return sum(1 for char in s if char in vowels)

    def count_consonants(self, s):
        """Counts the number of consonants in the input string."""
        vowels = "aeiouAEIOU"
        return sum(1 for char in s if char.isalpha() and char not in vowels)

    def word_count(self, s):
        """Returns the number of words in the input string."""
        return len(s.split())

    def is_palindrome(self, s):
        """Checks if the input string is a palindrome (ignoring case and non-alphanumeric characters)."""
        cleaned = ''.join(e for e in s if e.isalnum()).lower()
        return cleaned == cleaned[::-1]

    def char_frequencies(self, s):
        """Returns a dictionary of character frequencies in the input string."""
        return {char: s.count(char) for char in set(s)}

    def find_substring(self, s, substring):
        """Finds the first occurrence of a substring in the input string."""
        return s.find(substring)

    def split_by_delimiter(self, s, delimiter):
        """Splits the input string by the given delimiter."""
        return s.split(delimiter)

    def join_list_to_string(self, lst, delimiter):
        """Joins a list of strings into a single string, using the specified delimiter."""
        return delimiter.join(lst)

    def remove_punctuation(self, s):
        """Removes all punctuation characters from the input string."""
        return s.translate(str.maketrans('', '', string.punctuation))

    def truncate_string(self, s, length):
        """Truncates the input string to the specified length."""
        return s[:length] if len(s) > length else s

    def remove_digits(self, s):
        """Removes all digit characters from the input string."""
        return ''.join([i for i in s if not i.isdigit()])

    def get_all_links(self, soup):
        """Extracts all the 'href' links from an HTML soup object."""
        return [a['href'] for a in soup.find_all('a', href=True)]

