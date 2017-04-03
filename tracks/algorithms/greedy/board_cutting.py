


MOD = 10 ** 9 + 7

q = int(raw_input())
for _ in range(q):
    m, n = [int(x) for x in raw_input().split()]
    cys = [(int(x), 0) for x in raw_input().split()]
    cxs = [(int(x), 1) for x in raw_input().split()]

    cs = cys + cxs

    v = 1
    h = 1
    total = 0
    for cost, direction in sorted(cs, reverse=True):
        if direction == 0:
            mul = v
            h += 1
        else:
            mul = h
            v += 1

        total = (total + cost * mul) % MOD

    print total



