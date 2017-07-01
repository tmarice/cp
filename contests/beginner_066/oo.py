
import sys

def get_repeating_indexes(ax):
    elements = [-1] * (len(ax))

    for i, a in enumerate(ax):
        if elements[a] != -1:
            return elements[a], i
        else:
            elements[a] = i


MOD = 10 ** 9 + 7
memo = {}

def nck(a, b):
    if (a, b) in memo:
        return memo[(a,b)]
    elif b > a:
        return 0
    elif a == b or b == 0:
        return 1
    elif a-b < b:
        return nck(a, a-b)
    else:
        up = 1
        for i in range(a, a-b, -1):
            up *= i

        lo = 1
        for i in range(2, b+1):
            lo *= i

        memo[(a, b)] = up / lo % MOD
        return memo[(a, b)]


def main():
    n = int(raw_input())
    ax = [int(x) for x in raw_input().split()]

    i, j = get_repeating_indexes(ax)
    oob = i + (len(ax) - j - 1)

#    import pdb; pdb.set_trace()

    for i in range(1, n+2):
        if i == 1:
            print n
        else:
            print nck(n + 1, i) - nck(oob, i - 1)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 5 + 1)
    main()
