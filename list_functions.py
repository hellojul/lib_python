# Fonctions de manipulation de listes

def append_item(lst, item):
    lst.append(item)

def extend_list(lst, lst_to_add):
    lst.extend(lst_to_add)

def insert_item(lst, index, item):
    lst.insert(index, item)

def remove_item(lst, item):
    lst.remove(item)

def pop_item(lst, index=-1):
    return lst.pop(index)

def clear_list(lst):
    lst.clear()

def get_item_at_index(lst, index):
    return lst[index]

def find_index_of_item(lst, item):
    return lst.index(item) if item in lst else -1

def contains_item(lst, item):
    return item in lst

def count_occurrences(lst, item):
    return lst.count(item)

def get_first_n_elements(lst, n):
    return lst[:n]

def get_last_n_elements(lst, n):
    return lst[-n:]

def get_unique_items(lst):
    return list(set(lst))

def sort_list_ascending(lst):
    return sorted(lst)

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

def reverse_list(lst):
    return lst[::-1]

def shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst

def flatten_list(lst_of_lst):
    return [item for sublist in lst_of_lst for item in sublist]

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def map_function_to_list(lst, func):
    return list(map(func, lst))

def is_empty(lst):
    return len(lst) == 0

def has_duplicates(lst):
    return len(lst) != len(set(lst))

def get_common_items(lst1, lst2):
    return list(set(lst1) & set(lst2))

def list_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

def concat_lists(lst1, lst2):
    return lst1 + lst2

def interleave_lists(lst1, lst2):
    return [item for pair in zip(lst1, lst2) for item in pair]

def get_max(lst):
    return max(lst)

def get_min(lst):
    return min(lst)

def sum_list(lst):
    return sum(lst)

def average_list(lst):
    return sum(lst) / len(lst) if lst else 0

def rotate_list(lst, k):
    return lst[-k:] + lst[:-k]

