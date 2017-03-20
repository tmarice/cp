
def flood_fill(graph, n):
    n_roads = 0
    n_libs = 0

    visited = set()

    for i in range(n):
        if i in visited:
            continue

        s = [i]
        visited.add(i)
        n_libs += 1

        while s:
            cur_i = s.pop()

            for neigh in graph[cur_i]:
                if neigh not in visited:
                    visited.add(neigh)
                    s.append(neigh)
                    n_roads += 1

    return n_roads, n_libs


q = int(raw_input())

for _ in range(q):
    n, m, c_lib, c_road = [int(x) for x in raw_input().split()]
    graph = [[] for _ in range(n)]

    for _ in range(m):
        i, j = [int(x) for x in raw_input().split()]
        i -= 1
        j -= 1

        graph[i].append(j)
        graph[j].append(i)

    if c_lib <= c_road:
        print n * c_lib
    else:
        n_roads, n_libs = flood_fill(graph, n)
        print n_roads * c_road + n_libs * c_lib
