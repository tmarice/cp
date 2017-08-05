

def bs(a, target, lo, hi):
    if lo > hi:
        return

    mid = lo + (hi - lo) / 2

    if a[mid][0] == target:
        return mid
    elif a[mid][0] > target:
        return bs(a, target, lo, mid-1)
    else:
        return bs(a, target, mid+1, hi)


t = int(raw_input())

for _ in range(t):
    m = int(raw_input())
    n = int(raw_input())
    c = sorted([(int(x), i+1) for i, x in enumerate(raw_input().split())])

    for i in range(len(c)):
        target = m - c[i][0]
        t_i = bs(c, target, lo=i+1, hi=len(c)-1)
        if t_i is not None:
            print min(c[i][1], c[t_i][1]), max(c[i][1], c[t_i][1])
            break
