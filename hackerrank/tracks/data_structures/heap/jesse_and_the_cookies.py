import heapq

n, k = [int(x) for x in raw_input().split()]
a = [int(x) for x in raw_input().split()]

heapq.heapify(a)

s = 0

while len(a) > 1 and a[0] < k:
    x, y = heapq.heappop(a), heapq.heappop(a)
    z = x + 2*y
    heapq.heappush(a, z)
    s += 1

if a[0] >= k:
    print s
else:
    print -1





