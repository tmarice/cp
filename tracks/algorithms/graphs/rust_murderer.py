from collections import deque


def dfs(graph, n, s):
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

    for _ in range(m):
        x, y = [int(x) for x in raw_input().split()]

        x -= 1
        y -= 1

        graph[x].add(y)
        graph[y].add(x)

    s = int(raw_input())
    s -= 1

    dists = dfs(graph, n, s)

    for node, dist in dists.iteritems():
        if node != s:
            print dist,
    print
