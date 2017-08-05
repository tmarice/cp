
from collections import deque


memo = {}


def count_moves(n, i, j):
    if (i, j) in memo:
        return memo[(i, j)]

    q = deque()
    visited = set()

    dx = [i, j, j, i, -i, -j, -j, -i]
    dy = [j, i, -i, -j, -j, -i, i, j]
    ds = zip(dx, dy)

    q.appendleft(((0, 0), 0))
    visited.add((0, 0))

    while q:
        (a, b), d = q.pop()

        if a == n - 1 and b == n - 1:
            memo[(i, j)] = d
            memo[(j, i)] = d
            return d

        for da, db in ds:
            n_a = a + da
            n_b = b + db

            if n_a < 0 or n_a >= n or n_b < 0 or n_b >= n or (n_a, n_b) in visited:
                continue

            visited.add((n_a, n_b))
            q.appendleft(((n_a, n_b), d+1))

    memo[(i, j)] = -1
    memo[(j, i)] = -1
    return -1


n = int(raw_input())

for i in range(1, n):
    for j in range(1, n):
        print count_moves(n, i, j),
    print
