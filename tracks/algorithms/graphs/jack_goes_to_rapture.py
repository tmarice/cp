
import heapq

INF = 1000000000


def prim(graph, n):
    h = []
    visited = set([0])
    mst = {i:{} for i in range(n)}

    for node, c in graph[0].iteritems():
        heapq.heappush(h, (c, 0, node))

    while len(visited) < n and h:
        c, start, end = heapq.heappop(h)

        mst[start][end] = c
        mst[end][start] = c

        visited.add(end)

        if end == n - 1:
            break

        for other, cost in graph[end].iteritems():
            if other not in visited:
                heapq.heappush(h, (cost, end, other))

    return mst


def get_max_edge(graph, n):
    s = [0]
    parent = [None for _ in xrange(n)]
    parent[0] = 0

    while s:
        cur = s.pop()

        for other in graph[cur].iterkeys():
            if parent[other] is None:
                s.append(other)
                parent[other] = cur

    ret = 0
    cur = n - 1
    if parent[cur] is None:
        return None

    while parent[cur] != cur:
        ret = max(ret, graph[cur][parent[cur]])
        cur = parent[cur]

    return ret


n, m = [int(x) for x in raw_input().split()]
graph = {i:{} for i in xrange(n)}

for _ in xrange(m):
    x, y, r = [int(x) for x in raw_input().split()]

    x -= 1
    y -= 1

    graph[x][y] = r
    graph[y][x] = r


mst = prim(graph, n)
max_edge = get_max_edge(mst, n)
print max_edge if max_edge is not None else "NO PATH EXISTS"
