
import sys
from collections import defaultdict


graph = defaultdict(list)

def journey(probability, length, node, parent):
    children = [x for x in graph[node] if x != parent]
    n_children = len(children)

    if n_children == 0:
        return probability * length
    else:
        new_prob = probability / n_children
        return sum(journey(new_prob, length + 1, child, node) for child in children)


def main():
    n = int(input())

    for _ in range(n-1):
        u, v = (int(x) for x in input().split())
        graph[u].append(v)
        graph[v].append(u)

    print("{0:.6f}".format(journey(1.0, 0, 1, None)))


if __name__ == "__main__":
    sys.setrecursionlimit(100009)
    main()

