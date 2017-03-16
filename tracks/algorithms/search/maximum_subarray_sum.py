
import bisect
from itertools import islice


def find_gt(a, x):
    i = bisect.bisect_right(a, x)

    if i != len(a):
        return a[i]

    return 0


q = int(raw_input())

for _ in range(q):
    n, m = [int(x) for x in raw_input().split()]
    a = [int(x) for x in raw_input().split()]

    cumsums = [a[0] % m]
    out = a[0] % m
    sorted_cs = list(cumsums)

    for c in a[1:]:
        cs = (cumsums[-1] + c) % m
        cumsums.append(cs)

        other = find_gt(sorted_cs, cs)

        bisect.insort(sorted_cs, cs)

        out = max(out, (cs - other + m) % m)

    print out
