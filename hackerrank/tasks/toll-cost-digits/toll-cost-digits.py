"""
 * reduce everything mod 10 - including costs of whole paths
    * for every d={0, 9} how many pairs (x,y) s.t. there is path from x to y w/ cost d?

 * x->y w/ cost f  =>  y->x w/ cost -f (mod 10)
 * BFS/DFS through state graph - state is (y, d) - path from x to y w/ cost d
    * start from x (every node)
    * path x->x w/ cost 0
    * path x->y w/ cost d && edge y->z w/ cost f  => path x->z w/ cost d + f (mod 10)
    * TOO SLOW: O(N*(N+E))
"""

from collections import defaultdict
import sys


def do_dfs(source, adjl, n):
    states = defaultdict(set)

    def dfs(x, y, d):
        states[d].add((x, y))

        for v, c in adjl[y]:
            cost = (d % 10 + c % 10) % 10
            if (x, v) not in states[cost]:
                dfs(x, v, cost)

    for x in range(n):
        states[0].add((x, x))

    for v, c in adjl[source]:
        dfs(source, v, c)

    return [sum([1 for x, y in states[d] if x != y]) for d in range(10)]


def main():
    n, e = [int(x) for x in raw_input().split()]

    adjl = [[] for _ in range(n)]
    for _ in range(e):
        x, y, d = [int(a) for a in raw_input().split()]
        adjl[x-1].append((y-1, d % 10))
        adjl[y-1].append((x-1, -d % 10))

    pairs = [0] * 10
    for x in range(n):
        digits = do_dfs(x, adjl, n)
        pairs = [pairs[i] + digits[i] for i in range(10)]

    for x in pairs:
        print x


if __name__ == "__main__":
    sys.setrecursionlimit(1<<30)
    main()
