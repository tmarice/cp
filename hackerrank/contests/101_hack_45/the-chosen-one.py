import sys

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

memo = {}

def gcd_list(l):
    if len(l) == 1:
        return l[0]

    if len(l) == 2:
        if memo.get((l[0], l[1])):
            return memo[(l[0], l[1])]
        else:
            g = GCD(l[0], l[1])
            memo[(l[0], l[1])] = g
            return g

    return GCD(l[0], gcd_list(l[1:]))


def solve(n, m):
    gcds_front = []
    gcds_back = []

    for i in range(1, n+1):
        gcds_front.append(gcd_list(m[:i]))
        gcds_back.append(gcd_list(m[-i:]))

    print gcds_front
    print gcds_back

    for i in range(n):
        if i == 0:
            g = gcds_back[1]
        elif i == n-1:
            g = gcds_front[n-2]
        else:
            g = GCD(gcds_front[i-1], gcds_back[i+1])

        if m[i] % g:
            return g


def main():
    n = int(raw_input())
    a = [int(x) for x in raw_input().split()]

    r = solve(n, a)

    print r


if __name__ == "__main__":
    sys.setrecursionlimit(1<<30)
    main()
