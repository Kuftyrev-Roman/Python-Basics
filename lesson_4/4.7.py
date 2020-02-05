from functools import reduce


def fact(n):
    if n == 0:
        yield 1
    else:
        yield reduce(lambda n,y: n * y, range(1, n+1))


for el in fact(10):
    print(el)
