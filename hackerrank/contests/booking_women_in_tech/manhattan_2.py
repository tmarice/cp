
n, m, t = [int(x) for x in raw_input().split()]

city = []

for i in range(n):
    row = [int(x) for x in raw_input().split()]
    city.append(row)

sol_top = {}
for i in range(n):
    for j in range(m):
        up = sol_top.get((i-1, j))
        left = sol_top.get((i, j-1))

        n_candy = 0

        if up is not None:
            n_candy = max(n_candy, up)

        if left is not None:
            n_candy = max(n_candy, left)

        sol_top[(i, j)] = n_candy + city[i][j]

sol_bottom = {}
for i in reversed(range(0, n)):
    for j in reversed(range(0, m)):
        down = sol_bottom.get((i+1, j))
        right = sol_bottom.get((i, j+1))

        n_candy = 0

        if down is not None:
            n_candy = max(n_candy, down)

        if right is not None:
            n_candy = max(n_candy, right)

        sol_bottom[(i, j)] = n_candy + city[i][j]

import pdb; pdb.set_trace()
out = -1
if n - 1 + m - 1 > t:
    print "Too late"
else:
    for i in range(n):
        for j in range(m):
            steps = i + j + abs(n-1-i) + abs(m-1-j)

            luft = t - steps - 1

            n_candy = sol_top[(i, j)] + luft * city[i][j] + sol_bottom[(i, j)]
            out = max(out, n_candy)

    print out
