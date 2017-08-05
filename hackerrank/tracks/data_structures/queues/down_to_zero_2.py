
from collections import deque
from math import sqrt


def down_to_zero(n):
    q = deque()
    q.appendleft((n, 0))

    visited = set([n])

    while q:
        x, d = q.pop()
        if x == 0:
            return d

        for i in range(2, int(sqrt(x))+1):
            if x % i == 0:
                div = x / i
                if div not in visited:
                    visited.add(div)
                    q.appendleft((div, d+1))
        if x - 1 not in visited:
            visited.add(x-1)
            q.appendleft((x-1, d+1))


q = int(raw_input())

for _ in range(q):
    n = int(raw_input())

    print down_to_zero(n)
