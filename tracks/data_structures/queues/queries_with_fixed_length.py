
from collections import deque


class MaxQueue(object):

    def __init__(self, a=None):
        self._q = deque()
        self._max = deque()

        if a:
            for x in a:
                self.append(x)


    def pop(self):
        x = self._q.pop()

        if self._max[-1] == x:
            self._max.pop()

        return x


    def append(self, x):
        self._q.appendleft(x)

        while self._max and x >= self._max[0]:
            self._max.popleft()
        self._max.appendleft(x)


    @property
    def max(self):
        return self._max[-1]


n, q = [int(x) for x in raw_input().split()]
a = [int(x) for x in raw_input().split()]

for _ in range(q):
    d = int(raw_input())

    queue = MaxQueue(a[:d])
    res = queue.max

    for x in a[d:]:
        queue.pop()
        queue.append(x)
        res = min(res, queue.max)

    print res
