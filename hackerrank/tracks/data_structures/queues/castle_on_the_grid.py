
from collections import deque


def get_neighbors(r, c):
    cells = []
    # up
    i = r - 1
    while i >= 0 and m[i][c] != 'X':
        cells.append((i, c))
        i -= 1

    # down
    i = r + 1
    while i < n and m[i][c] != 'X':
        cells.append((i, c))
        i += 1

    # left
    i = c - 1
    while i >= 0 and m[r][i] != 'X':
        cells.append((r, i))
        i -= 1

    # right
    i = c + 1
    while i < n and m[r][i] != 'X':
        cells.append((r, i))
        i += 1

    return cells


def bfs(r_s, c_s, r_e, c_e):
    visited = set()
    q = deque()

    q.appendleft(((r_s, c_s), 0))

    while q:
        ((r, c), dist) = q.pop()

        if r == r_e and c == c_e:
            return dist

        for cell in get_neighbors(r, c):
            if cell not in visited:
                visited.add(cell)
                q.appendleft((cell, dist+1))


n = int(raw_input())
m = []
for _ in range(n):
    l = raw_input().strip()
    m.append(list(l))

a, b, c, d = [int(x) for x in raw_input().split()]

print bfs(a, b, c, d)
