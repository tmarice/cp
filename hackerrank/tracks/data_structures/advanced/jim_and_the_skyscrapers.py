
from collections import defaultdict


n = int(raw_input())
hs = [int(x) for x in raw_input().split()]

s = []
output = 0
for h in hs:
    count = defaultdict(int)

    while s and s[-1] < h:
        count[s.pop()] += 1

    s.append(h)
    for v in count.itervalues():
        output += v * (v-1)

count = defaultdict(int)
while s:
    count[s.pop()] += 1

for v in count.itervalues():
    output += v * (v-1)

print output


