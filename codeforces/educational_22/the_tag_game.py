
from collections import deque, defaultdict
from itertools import izip


graph = defaultdict(list)


def bfs(start_1, start_2):
    q = deque([start_1])
    dists = {start_1: 0}

    while q:
        cur = q.pop()

        for neigh in graph[cur]:
            if neigh not in dists:
                dists[neigh] = dists[cur] + 1
                q.appendleft(neigh)

    q = deque([(start_2, 0)])
    visited = set()
    out = 0

    while q:
        cur, d = q.pop()

        if d >= dists[cur]:
            continue
        else:
            out = max(out, dists[cur] * 2)

        for neigh in graph[cur]:
            if neigh not in visited:
                visited.add(neigh)
                q.appendleft((neigh, d+1))

    return out


def main():
    n, x = (int(x) for x in raw_input().split())

    for _ in range(n-1):
        a, b = (int(x) for x in raw_input().split())

        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    print bfs(0, x - 1)


main()
