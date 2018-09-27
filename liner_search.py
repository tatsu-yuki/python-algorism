def liner_search(n, data):
    for v in data:
        if v == n:
            return True
    return False


print(liner_search(4, [1, 2, 3, 4]))
