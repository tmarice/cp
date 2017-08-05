



def calculate_paths(graph, start, n):
    costs = {x: set() for x in xrange(n)}
    s = [(start, 0)]

    while s:
        node, pen = s.pop()

        for cost, other in graph[node]:
            new_cost = pen | cost

            if new_cost not in costs[other]:
                costs[other].add(new_cost)
                s.append((other, new_cost))

    return costs


n, m = [int(x) for x in raw_input().split()]
graph = [[] for _ in xrange(n)]

for _ in xrange(m):
    x, y, r = [int(x) for x in raw_input().split()]

    x -= 1
    y -= 1

    graph[x].append((r, y))
    graph[y].append((r, x))

a, b = [int(x) for x in raw_input().split()]
a -= 1
b -= 1

costs = calculate_paths(graph, a, n)
print min(costs[b]) if len(costs[b]) else -1
