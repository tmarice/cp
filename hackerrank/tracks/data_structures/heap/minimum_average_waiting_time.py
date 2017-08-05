from operator import itemgetter
import heapq

n = int(raw_input())
orders = []

for _ in range(n):
    t, l = [int(x) for x in raw_input().split()]
    orders.append((l, t))

orders.sort(key=itemgetter(1))
heap = []
cur_t = orders[0][1]
waits = []
i = 0

while i < n or heap: 

    while i < n and (len(heap) == 0 or orders[i][1] <= cur_t):
        heapq.heappush(heap, orders[i])
        i += 1

    l, t = heapq.heappop(heap)

    if t >= cur_t:
        waits.append(l)
        cur_t += l
    else:
        waits.append(cur_t - t + l)
        cur_t += l

print sum(waits) / len(waits)
