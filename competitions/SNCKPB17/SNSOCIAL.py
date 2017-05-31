
from collections import deque

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


def find_max(graph):
    ret = 0
    for row in graph:
        ret = max(ret, max(row))

    return ret


def bfs(n, m, graph):
    init_max = find_max(graph)

    visited = set()
    q = deque()
    for i in xrange(n):
        for j in xrange(m):
            if graph[i][j] == init_max:
                q.appendleft(((i, j), 0))
                visited.add((i, j))

    out = 0
    while q:
        (cur_i, cur_j), cur_m = q.pop()
        out = max(out, cur_m)

        for x,y in zip(dx, dy):
            neigh_i = cur_i + y
            neigh_j = cur_j + x

            if neigh_i >= 0 and neigh_i < n and neigh_j >= 0 and neigh_j < m:
                if (neigh_i, neigh_j) not in visited:
                    visited.add((neigh_i, neigh_j))
                    q.appendleft(((neigh_i, neigh_j), cur_m + 1))

    return out


def main():
    t = int(raw_input())

    for _ in range(t):
        n, m = [int(x) for x in raw_input().split()]
        graph = []

        for _ in range(n):
            graph.append([int(x) for x in raw_input().split()])

        print bfs(n, m, graph)


main()
