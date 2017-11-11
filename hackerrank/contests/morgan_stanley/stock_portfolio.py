
import sys

memo = {}
INF = 10 ** 9 + 7


def maximize(n, st, ls, rs):

    def choose(pos, prev_right):
        if pos < 0:
            return 0

        if (pos, prev_right) in memo:
            return memo[(pos, prev_right)]

        if pos + rs[pos] >= prev_right:
            return choose(pos - 1, prev_right)
        
        res = max(st[pos] + choose(pos - ls[pos] - 1, pos), choose(pos - 1, prev_right))
        memo[(pos, prev_right)] = res
        return res

    return choose(n -1, INF)


def main():
    n = int(input())
    st = [int(x) for x in input().split()]
    ls = [int(x) for x in input().split()]
    rs = [int(x) for x in input().split()]

    print(maximize(n, st, ls, rs))
     

if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
