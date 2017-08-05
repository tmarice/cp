
from collections import defaultdict


n, m, k = [int(x) for x in raw_input().split()]
intervals = defaultdict(list)

for _ in range(k):
    r, c1, c2 = [int(x) for x in raw_input().split()]
    intervals[r].append((c1, c2))

out = n * m
for inters in intervals.itervalues():
    inters = sorted(inters)

    start = inters[0][0]
    end = inters[0][1]
    for i in range(1, len(inters)):
        if start <= inters[i][0] <= end:
            end = max(end, inters[i][1])
        else:
            out -= end - start + 1
            start = inters[i][0]
            end = inters[i][1]

    out -= end - start + 1

print out
