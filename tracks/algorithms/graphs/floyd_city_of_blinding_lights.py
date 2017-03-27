
INF = 1000000000


def floyd_warshal(graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                n_d = graph[i][k] + graph[k][j]
                if graph[i][j] > n_d:
                    graph[i][j] = n_d



n, m = [int(x) for x in raw_input().split()]
graph = [[INF] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in xrange(m):
    x, y, r = [int(x) for x in raw_input().split()]

    x -= 1
    y -= 1

    graph[x][y] = r

floyd_warshal(graph)

q = int(raw_input())
for _ in range(q):
    n, m = [int(x) for x in raw_input().split()]
    n -= 1
    m -= 1

    print graph[n][m] if graph[n][m] != INF else -1
