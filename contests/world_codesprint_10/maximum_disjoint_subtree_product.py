

ROOT = 0

def get_max_diff(graph, ws_acc):
    s = [ROOT]
    visited = set([ROOT])

    max_diff = 0

    while s:
        cur = s.pop()

        for c in graph[cur]:
            if c not in visited:
                visited.add(c)
                s.append(c)

                pos = ws_acc[ROOT][0] - ws_acc[c][0]
                neg = ws_acc[ROOT][1] - ws_acc[c][1]

                max_diff = max(
                        max_diff,
                        pos * ws_acc[c][0],
                        neg * ws_acc[c][1])

    return max_diff


def accumulate(graph, ws, ws_acc, node, parent):
    if node != ROOT and len(graph[node]) == 1:
        ws_acc[node][0] = ws[node] if ws[node] > 0 else 0
        ws_acc[node][1] = 0 if ws[node] > 0 else -ws[node]
    else:
        for c in graph[node]:
            if c != parent:
                pos, neg = accumulate(graph, ws, ws_acc, c, node)
                ws_acc[node][0] += pos
                ws_acc[node][1] += neg

    return ws_acc[node]


def main():
    n = int(raw_input())

    ws = [int(x) for x in raw_input().split()]
    graph = [[] for _ in range(n)]
    ws_acc = []
    for w in ws:
        wt = [w if w > 0 else 0, 0 if w > 0 else -w]
        ws_acc.append(wt)

    for _ in range(n-1):
        u, v = [int(x) for x in raw_input().split()]

        u -= 1
        v -= 1

        graph[u].append(v)
        graph[v].append(u)

    accumulate(graph, ws, ws_acc, ROOT, None)

    print get_max_diff(graph, ws_acc)


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(1<<30)
    main()
