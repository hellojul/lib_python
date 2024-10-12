import random

class ListManipulator:
    """A class for performing various list manipulations."""

    def append_item(self, lst: list, item) -> None:
        """Appends an item to the end of the list."""
        lst.append(item)

    def extend_list(self, lst: list, lst_to_add: list) -> None:
        """Extends the list by appending elements from another list."""
        lst.extend(lst_to_add)

    def insert_item(self, lst: list, index: int, item) -> None:
        """Inserts an item at the specified index in the list."""
        lst.insert(index, item)

    def remove_item(self, lst: list, item) -> None:
        """Removes the first occurrence of an item from the list."""
        lst.remove(item)

    def pop_item(self, lst: list, index: int = -1):
        """Removes and returns the item at the specified index (or last item by default)."""
        return lst.pop(index)

    def clear_list(self, lst: list) -> None:
        """Removes all items from the list."""
        lst.clear()

    def get_item_at_index(self, lst: list, index: int):
        """Returns the item at the specified index."""
        return lst[index]

    def find_index_of_item(self, lst: list, item) -> int:
        """Finds the index of the first occurrence of an item, or returns -1 if not found."""
        return lst.index(item) if item in lst else -1

    def contains_item(self, lst: list, item) -> bool:
        """Checks if the list contains the specified item."""
        return item in lst

    def count_occurrences(self, lst: list, item) -> int:
        """Counts the occurrences of an item in the list."""
        return lst.count(item)

    def get_first_n_elements(self, lst: list, n: int) -> list:
        """Returns the first 'n' elements of the list."""
        return lst[:n]

    def get_last_n_elements(self, lst: list, n: int) -> list:
        """Returns the last 'n' elements of the list."""
        return lst[-n:]

    def get_unique_items(self, lst: list) -> list:
        """Returns a list of unique items from the input list."""
        return list(set(lst))

    def sort_list_ascending(self, lst: list) -> list:
        """Returns the list sorted in ascending order."""
        return sorted(lst)

    def sort_list_descending(self, lst: list) -> list:
        """Returns the list sorted in descending order."""
        return sorted(lst, reverse=True)

    def reverse_list(self, lst: list) -> list:
        """Returns the list in reverse order."""
        return lst[::-1]

    def shuffle_list(self, lst: list) -> list:
        """Shuffles the list randomly."""
        random.shuffle(lst)
        return lst

    def flatten_list(self, lst_of_lst: list) -> list:
        """Flattens a list of lists into a single list."""
        return [item for sublist in lst_of_lst for item in sublist]

    def remove_duplicates(self, lst: list) -> list:
        """Removes duplicates from the list while preserving order."""
        return list(dict.fromkeys(lst))

    def map_function_to_list(self, lst: list, func) -> list:
        """Applies a function to each item in the list."""
        return list(map(func, lst))

    def is_empty(self, lst: list) -> bool:
        """Checks if the list is empty."""
        return len(lst) == 0

    def has_duplicates(self, lst: list) -> bool:
        """Checks if the list contains duplicate items."""
        return len(lst) != len(set(lst))

    def get_common_items(self, lst1: list, lst2: list) -> list:
        """Returns the common items between two lists."""
        return list(set(lst1) & set(lst2))

    def list_difference(self, lst1: list, lst2: list) -> list:
        """Returns the difference between two lists (items in lst1 but not in lst2)."""
        return list(set(lst1) - set(lst2))

    def concat_lists(self, lst1: list, lst2: list) -> list:
        """Concatenates two lists."""
        return lst1 + lst2

    def interleave_lists(self, lst1: list, lst2: list) -> list:
        """Interleaves two lists (alternates elements from each)."""
        return [item for pair in zip(lst1, lst2) for item in pair]

    def get_max(self, lst: list):
        """Returns the maximum value in the list."""
        return max(lst)

    def get_min(self, lst: list):
        """Returns the minimum value in the list."""
        return min(lst)

    def sum_list(self, lst: list) -> int:
        """Returns the sum of all elements in the list."""
        return sum(lst)

    def average_list(self, lst: list) -> float:
        """Returns the average of the elements in the list."""
        return sum(lst) / len(lst) if lst else 0

    def rotate_list(self, lst: list, k: int) -> list:
        """Rotates the list by 'k' elements."""
        return lst[-k:] + lst[:-k]

