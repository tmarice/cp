

INF = 1000000000

n, m, q = [int(x) for x in raw_input().split()]

# (price, min stays, max stays)
offers = [[[0, 0, 0] for _ in range(n)] for _ in range(m)]

for k in range(3):
    for i in range(m):
        line = [int(x) for x in raw_input().split()]

        for j in range(n):
            offers[i][j][k] = line[j]

# (day, n_stays) -> min price
mins = {}

for i in range(n):
    for k in range(n):
        best = INF
        for j in range(m):
            if offers[j][i][0] > 0 and k >= offers[j][i][1] and k <= offers[j][i][2]:
                best = min(best, offers[j][i][0])

        if best != INF:
            mins[(i, k)] = best

for _ in range(q):
    c, l = [int(x) for x in raw_input().split()]
    c -= 1
    output = 0

    for i in range(l):
        r = mins.get((c+i, l))
        if r is None:
            output = -1
            break
        else:
            output += r

    print output
