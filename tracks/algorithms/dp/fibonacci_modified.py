

t1, t2, n = [int(x) for x in raw_input().split()]

ts = [t1, t2]

for i in xrange(2, n):
    ts.append(ts[i-1] ** 2 + ts[i-2])

print ts[-1]
