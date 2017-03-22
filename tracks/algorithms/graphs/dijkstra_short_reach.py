
import heapq
from collections import defaultdict


def dijkstra(graph, n, s):
    dist = {s: 0}
    visited = set()

    h = [(0, s)]

    while h:
        d, node = heapq.heappop(h)

        dist[node] = min(dist[node], d)
        visited.add(node)

        for other, r in graph[node].iteritems():
            if other not in visited:
                new_dist = dist[node] + r
                if other not in dist or new_dist < dist[other]:
                    dist[other] = new_dist
                    heapq.heappush(h, (new_dist, other))

    ret = []
    for node in xrange(1, n+1):
        sn = str(node)
        if sn not in dist:
            ret.append(-1)
        elif sn != s:
            ret.append(dist[sn])

    return ret


t = int(raw_input())

for _ in range(t):
    n, m = [int(x) for x in raw_input().split()]

    graph = {str(x): {} for x in xrange(1, n+1)}
    for _ in range(m):
        x, y, r = raw_input().split()
        r = int(r)

        if y in graph[x]:
            graph[x][y] = min(graph[x][y], r)
        else:
            graph[x][y] = r

        if x in graph[y]:
            graph[y][x] = min(graph[y][x], r)
        else:
            graph[y][x] = r

    s = raw_input()

    dist = dijkstra(graph, n, s)

    for d in dist:
        print d,
    print
