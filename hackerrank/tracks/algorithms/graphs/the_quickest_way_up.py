
from collections import deque

t = int(raw_input())

for _ in range(t):
    nexts = {}

    n_l = int(raw_input())
    for _ in range(n_l):
        a, b = [int(x) for x in raw_input().split()]
        nexts[a] = b

    n_s = int(raw_input())
    for _ in range(n_s):
        a, b = [int(x) for x in raw_input().split()]
        nexts[a] = b

    visited = set([1])
    q = deque([(1, 0)])

    out = -1
    while q:
        cur, dist = q.pop()

        if cur == 100:
            out = dist
            break

        for i in range(1, 7):
            step = cur + i

            if step in nexts:
                step = nexts[step]

            if step not in visited:
                visited.add(step)
                q.appendleft((step, dist+1))

    print out
