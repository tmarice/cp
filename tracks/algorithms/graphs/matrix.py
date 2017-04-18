
INF = 1000000000

out = 0
def dfs(graph, robots, node, prev, cur_min):
    global out

    if node in robots:
        if prev is not None:
            out += cur_min
            cur_min = INF

        prev = node

    for neigh, dist in graph[node].iteritems():
        if neigh not in visited:
            visited.add(neigh)
            dfs(graph, robots, neigh, prev, min(dist, cur_min))


n, k = [int(x) for x in raw_input().split()]

graph = {x: {} for x in range(n)}
for _ in range(n-1):
    x, y, r = [int(x) for x in raw_input().split()]

    graph[x][y] = r
    graph[y][x] = r

robots = set()
for _ in range(k):
    x = int(raw_input())
    robots.add(x)
    s = x

visited = set([s])
dfs(graph, robots, s, None, INF)

print out
