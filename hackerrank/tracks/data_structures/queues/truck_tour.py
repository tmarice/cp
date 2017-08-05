# not solved w/ queue, but w/ stack

n = int(raw_input())

s = []
for i in range(n):
    p, d = [int(x) for x in raw_input().split()]
    s.append((d - p, i))

output = 0
cur = 0

while s:
    diff, i = s.pop()
    cur += diff

    if cur <= 0:
        output = i
        cur = 0

print output

