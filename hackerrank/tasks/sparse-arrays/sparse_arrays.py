from collections import defaultdict

n = int(raw_input())
strings = defaultdict(int)

for _ in range(n):
    strings[raw_input()] += 1

q = int(raw_input())

for _ in range(q):
    s = raw_input()
    print strings[s]
