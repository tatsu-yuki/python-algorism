def binary_search(x, ls):
    low = 0
    high = len(ls) - 1
    while low <= high:
        middle = (low + high) / 2
        middle = int(middle)
        if x == ls[middle]:
            return True
        elif x > ls[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return False


print(binary_search(44, [11, 22, 33, 44, 55, 66, 77, 88, 99]))
