
dc = [0, 1, 1, 1, 0, -1, -1, -1]
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
ds = zip(dc, dr)

def count_region(i, j):
    s = [(i, j)]
    count = 0
    k[i][j] = 0

    while s:
        r, c = s.pop()
        count += 1

        for dc, dr in ds:
            n_r = r + dr
            n_c = c + dc

            if n_r >= 0 and n_r < n and n_c >= 0 and n_c < m and k[n_r][n_c] == 1:
                s.append((n_r, n_c))
                k[n_r][n_c] = 0

    return count


n = int(raw_input())
m = int(raw_input())

k = []
for _ in range(n):
    k.append([int(x) for x in raw_input().split()])


out = 0
for i in range(n):
    for j in range(m):
        if k[i][j] == 1:
            out = max(out, count_region(i, j))

print out
