
# NOTE: no need for UF, this can be solved by DFS

n = int(raw_input())

graph = [[] for _ in range(2*n)]

for _ in range(n):
    a, b = [int(x) for x in raw_input().split()]
    a -= 1
    b -= 1

    graph[a].append(b)
    graph[b].append(a)

visited = set()
min_component = 15001
max_component = 0

for start in range(2*n):
    if start in visited:
        continue

    size = 0
    stack = [start]
    visited.add(start)

    while stack:
        x = stack.pop()
        size += 1

        for neigh in graph[x]:
            if neigh not in visited:
                stack.append(neigh)
                visited.add(neigh)

    if size > 1:
        max_component = max(max_component, size)
        min_component = min(min_component, size)

print min_component, max_component
