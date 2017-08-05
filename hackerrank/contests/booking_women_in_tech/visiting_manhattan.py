

def dist(x, y, landmarks):
    d = 0
    for l in landmarks:
        d += abs(x - l[0]) + abs(y - l[1])

    return d


x, y, l, h = [int(x) for x in raw_input().split()]
landmarks = []
for _ in range(l):
    lx, ly = [int(x) for x in raw_input().split()]
    landmarks.append((lx, ly))

m = 1000000000
for _ in range(h):
    hx, hy = [int(x) for x in raw_input().split()]
    m = min(m, dist(hx, hy, landmarks))

print m

