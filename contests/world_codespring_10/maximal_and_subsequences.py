

import math


MOD = 10 ** 9 + 7


def C(n, k):
    if n - k < k:
        k = n - k

    num = 1
    den = 1

    for i in range(1, k+1):
        num *= n - i + 1
        den *= i

    return num / den


def main():
    n, k = [int(x) for x in raw_input().split()]
    xs = []
    hi = 0

    for _ in range(n):
        x = int(raw_input())
        xs.append(x)
        hi = max(hi, x)

    if hi == 0:
        print 0
        print C(n, k)
        return

    max_mask = 2 ** int(math.log(hi, 2))

    old_xs = xs
    max_n = 0
    max_and = 0

    while max_mask:
        new_xs = []
        for x in old_xs:
            if x & max_mask:
                new_xs.append(x)

        l = len(new_xs)
        if l >= k:
            max_and |= 1
            old_xs = new_xs
            max_n = C(l, k)

        max_and <<= 1
        max_mask >>= 1

    max_and >>= 1
    if max_and == 0:
        max_n = C(n, k) % MOD

    print max_and 
    print max_n % MOD


if __name__ == "__main__":
    main()



