

from collections import defaultdict


def dfs(graph, start, visited):
    s = [start]
    visited.add(start)
    r = 1

    while s:
        cur = s.pop()

        for neigh in graph[cur]:
            if neigh not in visited:
                visited.add(neigh)
                s.append(neigh)
                r += 1

    return r


def main():
    n, m = [int(x) for x in raw_input().split()]

    graph = defaultdict(set)
    for _ in range(m):
        u, v = [int(x) for x in raw_input().split()]

        graph[u].add(v)
        graph[v].add(u)

    visited = set()
    out = 0

    for i in range(n):
        if i not in visited:
            out = max(out, dfs(graph, i, visited))

    print out


if __name__ == "__main__":
    main()
