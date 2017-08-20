
from math import log, exp


MOD = 10 ** 9 + 7

def dp(graph, n, start, end, k):
    prev_table = [[MOD] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                prev_table[i][j] = graph[i][j]


    print(prev_table)
    for e in range(2, k+1):
        cur_table = [[MOD] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for a in range(n):
                    if (graph[i][a] != MOD and 
                        i != a and j != a and 
                        prev_table[a][j] != MOD):
                        cur_table[i][j] = min(
                            cur_table[i][j],
                            prev_table[a][j] + graph[i][a]
                        )
        print(cur_table)
        prev_table = cur_table

    return cur_table[start][end]


def main():
    n = int(input())
    x, s, f, m = (int(a) for a in input().split())

    graph = []
    for _ in range(n):
        graph.append([-log(int(a)) if a != '0' else MOD for a in input().split()])

    coef = dp(graph, n, s, f, m)

    print(x * round(exp(-coef)) % MOD)


if __name__ == "__main__":
    main()

