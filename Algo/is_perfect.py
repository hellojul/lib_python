from get_dividers import get_dividers

def is_perfect(nb):
    """
    Tester si un nombre est parfait.
    """
    if sum(get_dividers(nb)[:-1]) == nb:
        return True
    return False


if __name__ == '__main__':
    try:
        cmd = int(input('Enter number: '))
        if is_perfect(cmd):
            print(f'\n{cmd} is a perfect number.')
        else:
            print(f'\n{cmd} is not a perfect number.')
    except:
        print('Error.')
