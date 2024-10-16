import random

def append_item(self, lst: list, item) -> None:
    """Ajoute un élément à la fin de la liste."""
    lst.append(item)

def extend_list(self, lst: list, lst_to_add: list) -> None:
    """Étend la liste en ajoutant des éléments d'une autre liste."""
    lst.extend(lst_to_add)

def insert_item(self, lst: list, index: int, item) -> None:
    """Insère un élément à l'indice spécifié dans la liste."""
    lst.insert(index, item)

def remove_item(self, lst: list, item) -> None:
    """Supprime la première occurrence d'un élément de la liste."""
    lst.remove(item)

def pop_item(self, lst: list, index: int = -1):
    """Supprime et retourne l'élément à l'indice spécifié (ou le dernier par défaut)."""
    return lst.pop(index)

def clear_list(self, lst: list) -> None:
    """Supprime tous les éléments de la liste."""
    lst.clear()

def get_item_at_index(self, lst: list, index: int):
    """Retourne l'élément à l'indice spécifié."""
    return lst[index]

def find_index_of_item(self, lst: list, item) -> int:
    """Trouve l'indice de la première occurrence d'un élément, ou retourne -1 si non trouvé."""
    return lst.index(item) if item in lst else -1

def contains_item(self, lst: list, item) -> bool:
    """Vérifie si la liste contient l'élément spécifié."""
    return item in lst

def count_occurrences(self, lst: list, item) -> int:
    """Compte le nombre d'occurrences d'un élément dans la liste."""
    return lst.count(item)

def get_first_n_elements(self, lst: list, n: int) -> list:
    """Retourne les 'n' premiers éléments de la liste."""
    return lst[:n]

def get_last_n_elements(self, lst: list, n: int) -> list:
    """Retourne les 'n' derniers éléments de la liste."""
    return lst[-n:]

def get_unique_items(self, lst: list) -> list:
    """Retourne une liste des éléments uniques de la liste donnée."""
    return list(set(lst))

def sort_list_ascending(self, lst: list) -> list:
    """Retourne la liste triée par ordre croissant."""
    return sorted(lst)

def sort_list_descending(self, lst: list) -> list:
    """Retourne la liste triée par ordre décroissant."""
    return sorted(lst, reverse=True)

def reverse_list(self, lst: list) -> list:
    """Retourne la liste dans l'ordre inverse."""
    return lst[::-1]

def shuffle_list(self, lst: list) -> list:
    """Mélange la liste de manière aléatoire."""
    random.shuffle(lst)
    return lst

def flatten_list(self, lst_of_lst: list) -> list:
    """Aplatie une liste de listes en une seule liste."""
    return [item for sublist in lst_of_lst for item in sublist]

def remove_duplicates(self, lst: list) -> list:
    """Supprime les doublons de la liste tout en préservant l'ordre."""
    return list(dict.fromkeys(lst))

def map_function_to_list(self, lst: list, func) -> list:
    """Applique une fonction à chaque élément de la liste."""
    return list(map(func, lst))

def is_empty(self, lst: list) -> bool:
    """Vérifie si la liste est vide."""
    return len(lst) == 0

def has_duplicates(self, lst: list) -> bool:
    """Vérifie si la liste contient des éléments en double."""
    return len(lst) != len(set(lst))

def get_common_items(self, lst1: list, lst2: list) -> list:
    """Retourne les éléments communs entre deux listes."""
    return list(set(lst1) & set(lst2))

def list_difference(self, lst1: list, lst2: list) -> list:
    """Retourne la différence entre deux listes (éléments dans lst1 mais pas dans lst2)."""
    return list(set(lst1) - set(lst2))

def concat_lists(self, lst1: list, lst2: list) -> list:
    """Concatène deux listes."""
    return lst1 + lst2

def interleave_lists(self, lst1: list, lst2: list) -> list:
    """Entrelace deux listes (alterne les éléments de chaque liste)."""
    return [item for pair in zip(lst1, lst2) for item in pair]

def get_max(self, lst: list):
    """Retourne la valeur maximale de la liste."""
    return max(lst)

def get_min(self, lst: list):
    """Retourne la valeur minimale de la liste."""
    return min(lst)

def sum_list(self, lst: list) -> int:
    """Retourne la somme de tous les éléments de la liste."""
    return sum(lst)

def average_list(self, lst: list) -> float:
    """Retourne la moyenne des éléments de la liste."""
    return sum(lst) / len(lst) if lst else 0

def rotate_list(self, lst: list, k: int) -> list:
    """Fait pivoter la liste de 'k' éléments."""
    return lst[-k:] + lst[:-k]

