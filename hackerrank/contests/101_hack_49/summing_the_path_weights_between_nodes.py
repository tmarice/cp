
from collections import defaultdict


def solve(n, graph, total_red, total_black, count_red, count_black):
    ret = 0
    p = False


    for _ in range(n-1):
        if not p:
            for f, edges in graph.iteritems():
                if len(edges) == 1:
                    # cur
                    cur = f, edges.keys()[0], edges.values()[0]
                    break
            else:
                return ret

        p = False

        ret += count_black[cur[0]] * (total_red - count_red[cur[0]]) * cur[2]
        ret += count_red[cur[0]] * (total_black - count_black[cur[0]]) * cur[2]
        count_black[cur[1]] += count_black[cur[0]]
        count_red[cur[1]] += count_red[cur[0]]

        del graph[cur[0]]
        del graph[cur[1]][cur[0]]

        if len(graph[cur[1]]) == 1:
            cur = cur[1], graph[cur[1]].keys()[0], graph[cur[1]].values()[0]
            p = True


    return ret


def main():
    n = int(raw_input())

    count_black = []
    count_red = []
    total_black = 0
    total_red = 0
    for c in raw_input().split():
        if c == '1':
            count_black.append(1)
            count_red.append(0)
            total_black += 1
        else:
            count_black.append(0)
            count_red.append(1)
            total_red += 1

    graph = defaultdict(dict)
    for _ in range(n-1):
        u, v, w = [int(x) for x in raw_input().split()]
        u -= 1
        v -= 1

        graph[u][v] = w
        graph[v][u] = w

    print solve(n, graph, total_red, total_black, count_red, count_black)


main()


