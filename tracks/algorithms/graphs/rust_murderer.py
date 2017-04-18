
from collections import deque


def dfs(graph, not_visited, n, s):
    dists = {s: 0}

    not_visited = {x for x in range(n)}
    not_visited.remove(s)
    q = deque([s])

    while q:
        cur = q.popleft()
        cur_dist = dists[cur]

        removal = []
        for neigh in not_visited:
            if neigh not in graph[cur]:
                dists[neigh] = cur_dist + 1
                q.append(neigh)
                removal.append(neigh)

        for x in removal:
            not_visited.remove(x)

    return dists


t = int(raw_input())

for _ in range(t):
    n, m = [int(x) for x in raw_input().split()]

    graph = {x:set() for x in range(n)}
    not_visited = set()

    for _ in range(m):
        x, y = [int(x) for x in raw_input().split()]

        x -= 1
        y -= 1

        not_visited.add(x)
        not_visited.add(y)

        graph[x].add(y)
        graph[y].add(x)

    s = int(raw_input())
    s -= 1

    if s in not_visited:
        not_visited.remove(s)
    dists = dfs(graph, not_visited, n, s)

    for i in range(n):
        if i != s:
            if i in dists:
                print dists[i],
            else:
                print 1,
    print
