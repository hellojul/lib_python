from is_prime import is_prime


def get_primes_list(inf, sup):
    """
    Liste des nombres premiers dans un intervalle.
    """
    if inf >= sup:
        return 'Error.'

    primes_list = []

    for nb in range(inf, sup+1):
        if is_prime(nb):
            primes_list.append(nb)

    return primes_list


if __name__ == '__main__':
    try:
        cmd_1 = int(input('Enter number inf: '))
        cmd_2 = int(input('Enter number sup: '))
        print(get_primes_list(cmd_1, cmd_2))
    except:
        print('Error')
