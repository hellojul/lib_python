def bubble_sort(lst):
    permutation = True
    j = 0
    while permutation:
        permutation = False
        j = j + 1
        for i in range(0, len(lst)-j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                permutation = True

    return lst
