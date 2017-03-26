
from collections import deque


class Average(object):
    def __init__(self, n):
        self._n = n
        self._q = deque()
        self._sum = 0


    def push(self, x):
        self._sum += x
        self._q.append(x)

        if len(self._q) > self._n:
            self._sum -= self._q.popleft()


    @property
    def avg(self):
        return round(float(self._sum) / min(self._n, len(self._q)), 2)


n = int(raw_input())
ps = [int(x) for x in raw_input().split()]

stma = Average(60)
ltma = Average(300)

for i, d in enumerate(ps):
    if i >= 300:
        old_stma = stma.avg
        old_ltma = ltma.avg

        stma.push(d)
        ltma.push(d)
        
        new_stma = stma.avg
        new_ltma = ltma.avg

        if (old_stma > old_ltma and new_stma <= new_ltma or
            old_stma < old_ltma and new_stma >= new_ltma or
            old_stma == old_ltma and new_stma != new_ltma):
            print i+1, new_stma, new_ltma
    else:
        stma.push(d)
        ltma.push(d)
