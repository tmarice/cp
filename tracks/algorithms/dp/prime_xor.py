

from math import sqrt
from collections import defaultdict


MOD = 10 ** 9 + 7

def count(xs, primes, n):
    import pdb; pdb.set_trace()
    dp = [0] * (2 ** 13)

    for x in xs:
        dp[x] = 1

    for x in xs:
        for i, y in enumerate(dp):
            if y:
                n_x = x ^ i
                dp[n_x] = (dp[n_x] + y) % MOD

    return sum(x for x in dp if x in primes)


def is_prime(x):
    for i in range(2, int(sqrt(x))):
        if x % i == 0:
            return False

    return True

def main():
    q = int(raw_input())

    primes = set(x for x in range(2, 2 ** 13) if is_prime(x))

    for _ in range(q):
        n = int(raw_input())
        xs = [int(x) for x in raw_input().split()]

        print count(xs, primes, n)


if __name__ == "__main__":
    main()


