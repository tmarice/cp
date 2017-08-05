import itertools


def prime(x, primes):
    end = x ** 0.5

    for p in primes:
        if p > end:
            break

        if x % p == 0:
            return False

    return True


def get_primes(n):
    primes = [2]

    i = 3
    while len(primes) < n:
        if prime(i, primes):
            primes.append(i)

        i += 1

    return primes



n, q = [int(x) for x in raw_input().split()]
a = [int(x) for x in raw_input().split()]

primes = get_primes(q)

bs = []

for p in primes:
    new_a = []

    b = []
    bs.append(b)

    while a:
        x = a.pop()
        if x % p == 0:
            b.append(x)
        else:
            new_a.append(x)

    a = new_a

bs.append(a)

for stack in bs:
    while stack:
        print stack.pop()
