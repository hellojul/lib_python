from is_prime import is_prime
from get_dividers import get_dividers

def get_prime_dividers(nb):
    """
    Liste des diviseurs qui sont des nombres premiers.
    """
    dividers_prime_list = []
    for divider in get_dividers(nb):
        if is_prime(divider):
            dividers_prime_list.append(divider)
    return dividers_prime_list


if __name__ == '__main__':
    try:
        cmd = int(input('Enter number: '))
        print(f'\n{get_prime_dividers(cmd)}')
    except:
        print('Error.')
