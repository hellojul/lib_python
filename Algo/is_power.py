def is_power(n, p):
    """
    Tester si un nombre est la puissance d'un autre nombre.
    """
    for i in range(1, n):
        if i**p > n:
            return False
        elif i**p == n:
            return True


if __name__ == '__main__':
    try:
        cmd_1 = int(input('Number 1: '))
        cmd_2 = int(input('Number 2: '))
        print(f'\n{is_power(cmd_1, cmd_2)}')
    except:
        print('Error.')
