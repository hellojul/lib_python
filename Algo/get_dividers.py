def get_dividers(nb):
    """
    Obtenir la liste des diviseurs d'un nombre entier.
    """
    dividers_list = []
    for d in range(1, nb+1):
        if nb % d == 0:
            dividers_list.append(d)
    return dividers_list


if __name__ == '__main__':
    try:
        cmd = int(input('Enter number: '))
        print(f'\nList dividers:\n{get_dividers(cmd)}')
    except:
        print(f'Error')
