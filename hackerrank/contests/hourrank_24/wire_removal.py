
from collections import defaultdict
import sys

tp = 0

def solve(graph, n):
    count = {}

    # assign depths
    def get_count(node, parent, prob):
        global tp
        tp += prob

        if graph[node] == [parent]:
            count[node] = 1
            return 1
        else:
            s = 1
            for child in graph[node]:
                if child != parent:
                    s += get_count(child, node, prob + 1)

            count[node] = s
            return s

    get_count('1', '0', 0)

    total_prob = 0.0

    s = [('1', 0, '0')]
    while s:
        node, depth, parent = s.pop()

        total_prob += depth * (n - count[node])

        for child in graph[node]:
            if child != parent:
                s.append((child, depth + 1, node))

    return total_prob / tp


def main():
    graph = defaultdict(list)

    n = int(input())

    for _ in range(n - 1):
        a, b = (x for x in input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(solve(graph, n))


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()


