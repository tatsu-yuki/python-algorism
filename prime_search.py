prime_list = [2]

for x in range(3, 100, 2):
    for y in prime_list:
        if x % y == 0:
            break
    else:
        prime_list.append(x)

print(prime_list)
