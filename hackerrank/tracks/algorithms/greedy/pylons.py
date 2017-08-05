
n, k = [int(x) for x in raw_input().split()]
towers = [int(x) for x in raw_input().split()]

start = 0
out = 0
i = 0
max_allowed = k - 1

while i < n - 1:
    s = None
    end = min(start + max_allowed + 1, n)

    if start + k > n:
        break

    for i in range(start, end):
        if towers[i] == 1:
            s = i

    if s is None:
        out = -1
        break
    else:
        out += 1
        start = s + 1
        max_allowed = 2 * (k-1)

print out





