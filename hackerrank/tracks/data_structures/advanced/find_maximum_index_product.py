
n = int(raw_input())

a = [int(x) for x in raw_input().split()]

s = []

out = 0

for x, i in zip(a, range(1, len(a) + 1)):
    while s and s[-1][0] < x:
        start = 0
        temp, _ = s.pop()

        while s and s[-1][0] == temp:
            s.pop()

        if s:
            start = s[-1][1]

        out = max(out, start * i)

    s.append((x, i))

print out
