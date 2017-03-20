

memo = {}
INF = 1000000000

def min_cost(i, k, s):
    if (i, k, s) in memo:
        return memo[(i, k, s)]

    if k < 0:
        return INF

    if i == n:
        return 0

    r = min(
            min_cost(i+1, k, s) + (poles[i][0] - poles[s][0]) * poles[i][1],
            min_cost(i+1, k-1, i)
    )
    memo[(i, k, s)] = r

    return r


n, k = [int(x) for x in raw_input().split()]

poles = []
for _ in range(n):
    poles.append([int(x) for x in raw_input().split()])

print min_cost(1, k-1, 0)
