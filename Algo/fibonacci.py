values = {1: 1, 2: 1}

def fibonacci(n):
    global values
    if not n in values.keys():
        values[n] = fibonacci(n-1) + fibonacci(n-2)
    return values[n]


if __name__ == '__main__':
    try:
        cmd = int(input('Enter number: '))
        if cmd > 300:
            exit()

        print('\n')
        for i in range(1, cmd):
            print(fibonacci(i))
    except:
        print('Error.')
