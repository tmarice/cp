

def get_edges(x):
    bits = bin(x)[2:]
    edges = []

    for i in range(len(bits) - 1):
        for j in range(i+1, len(bits)):
            if bits[i] == '1' and bits[j] == '1':
                edges.append((i, j))

    return edges


def get_subset(ds, i):
    vertices = []

    b = bin(i)[2:]
    for j in range(len(b)):
        if b[j] == '1':
            vertices.append(ds[j])

    return vertices


def make_graph(edges, vertices):
    graph = {x: [] for x in range(64)}

    for v in vertices:
        for a, b in edges[v]:
            graph[a].append(b)
            graph[b].append(a)

    return graph


def get_cc(graph):
    visited = set()
    ret = 0

    for v in graph:
        if v in visited:
            continue

        s = [v]
        visited.add(v)
        ret += 1

        while s:
            cur = s.pop()

            for neigh in graph[cur]:
                if neigh not in visited:
                    visited.add(neigh)
                    s.append(neigh)

    return ret


n = int(raw_input())
ds = [int(x) for x in raw_input().split()]

edges = {}
for d in ds:
    edges[d] = get_edges(d)

out = 0
for i in range(2**(n+1)):
    vertices = get_subset(ds, i)
    graph = make_graph(edges, vertices)
    out += get_cc(graph)

print out / 2
