
from collections import defaultdict


def map_graph(graph, points):
    for k, v in graph.iteritems():
        if len(v) == 1:
            start = k
            break

    parent = None
    current = start
    i = 0

    mapping = {}

    while current != None:
        mapping[current] = points[i][2]
        i += 1

        for other in graph[current]:
            if other != parent:
                parent = current
                current = other
                break
        else:
            break

    return mapping



def main():
    n = int(raw_input())

    graph = defaultdict(list)

    for _ in range(n-1):
        u, v = [int(x) for x in raw_input().split()]
        graph[u].append(v)
        graph[v].append(u)

    points = []

    for i in range(n):
        a, b = [int(x) for x in raw_input().split()]
        points.append((a, b, i+1))

    points.sort()

    mapping = map_graph(graph, points)

    for k in sorted(mapping.keys()):
        print mapping[k],


if __name__ == "__main__":
    main()


