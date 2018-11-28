def fizzbuzz_forloop(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


print(fizzbuzz_forloop(100))


def fizzbuzz_generator(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            yield 'FizzBuzz'
        elif i % 5 == 0:
            yield 'Buzz'
        elif i % 3 == 0:
            yield 'Fizz'
        else:
            yield i


for x in fizzbuzz_generator(100): print(x)
