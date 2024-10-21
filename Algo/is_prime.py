def is_prime(nb):
    """
    Tester si un nombre est premier.
    https://fr.wikipedia.org/wiki/Nombre_premier
    """
    if nb < 2:
        return False
    for d in range(2, nb):
        if nb % d  == 0:
            return False
    return True


if __name__ == '__main__':
    try:
        cmd = int(input('Enter number: '))

        if is_prime(cmd):
            print(f'\n{cmd} is prime.')
        else:
            print(f'\n{cmd} is not prime.')
    except:
        print('Error.')
