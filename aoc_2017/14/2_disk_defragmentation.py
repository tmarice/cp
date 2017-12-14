
from functools import reduce
from operator import xor


N = 256

DS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def get_dense_hash(s):
    return [reduce(xor, s[i * 16: i * 16 + 16])
            for i in range(16)]


def reverse(s, start, end, steps):
    if steps == 0:
        return

    s[start], s[end] = s[end], s[start]

    reverse(s, (start + 1) % N, (end - 1 + N) % N, steps - 1)


def knot_hash(s):
    lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
    s = list(range(N))
    skip = 0
    cur_pos = 0

    for _ in range(64):
        for l in lengths:
            reverse(s, cur_pos, (cur_pos + l - 1) % N, l // 2)
            cur_pos = (cur_pos + l + skip) % N
            skip += 1

    dh = get_dense_hash(s)
    kh = ''.join("{0:02x}".format(h) for h in dh)

    return kh


def generate_graph(s):
    graph = []

    for i in range(128):
        kh = knot_hash("{0}-{1}".format(s, i))
        graph.append("{0:0128b}".format(int(kh, 16)))

    return graph


def dfs(start, graph, visited):
    s = [start]
    visited[start[0]][start[1]] = 1

    while s:
        cur_i, cur_j = s.pop()

        for di, dj in DS:
            new_i = cur_i + di
            new_j = cur_j + dj

            if 0 <= new_i < 128 and 0 <= new_j < 128:
                if graph[new_i][new_j] == '1' and not visited[new_i][new_j]:
                    visited[new_i][new_j] = 1
                    s.append((new_i, new_j))


def count_groups(graph):
    groups = 0
    visited = [[0] * 128 for _ in range(128)]

    for i in range(128):
        for j in range(128):
            if graph[i][j] == '1' and not visited[i][j]:
                dfs((i, j), graph, visited)
                groups += 1

    return groups


def solve(s):
    graph = generate_graph(s)

    result = count_groups(graph)

    return result


def main():
    s = input().strip()

    d = solve(s)

    print(d)



if __name__ == "__main__":
    main()
