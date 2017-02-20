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

for p in primes:
    ai = []
    for x in a:
        if x % 
