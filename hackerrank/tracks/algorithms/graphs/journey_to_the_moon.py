
n, p = [int(x) for x in raw_input().split()]
graph = [[] for _ in range(n)]

for _ in range(p):
    a, b = [int(x) for x in raw_input().split()]

    graph[a].append(b)
    graph[b].append(a)


visited = set()
components = []
cumsum = 0
s = []

for i in range(n):
    if i in visited:
        continue

    s.append(i)
    visited.add(i)
    c = 1

    while s:
        cur = s.pop()

        for neigh in graph[cur]:
            if neigh not in visited:
                visited.add(neigh)
                s.append(neigh)
                c += 1

    components.append(c)
    cumsum += c


out = 0
for c in components:
    out += c * (cumsum - c)


print out / 2
