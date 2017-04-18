

n, k = [int(x) for x in raw_input().split()]
cs = [int(x) for x in raw_input().split()]
cs.sort()


m = 1
cur_k = k
out = 0
for i in range(n-1, -1, -1):
    out += m * cs[i]

    cur_k -= 1
    if cur_k <= 0:
        cur_k = k
        m += 1

print out



