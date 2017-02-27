import heapq


class MedianFinder(object):

    def __init__(self):
        self._lt = [] # max heap
        self._ge = [] # min heap


    def add(self, x):
        if len(self._ge) == 0 or x >= self._ge[0]:
            heapq.heappush(self._ge, x)
        else:
            heapq.heappush(self._lt, -x)

        if len(self._lt) > len(self._ge) + 1:
            heapq.heappush(self._ge, -heapq.heappop(self._lt))
        if len(self._ge) > len(self._lt) + 1:
            heapq.heappush(self._lt, -heapq.heappop(self._ge))


    @property
    def median(self):
        if len(self._lt) == len(self._ge):
            return (-self._lt[0] + self._ge[0]) / 2.
        elif len(self._lt) > len(self._ge):
            return -self._lt[0]
        else:
            return self._ge[0]


n = int(raw_input())
mf = MedianFinder()

for _ in range(n):
    x = int(raw_input())
    mf.add(x)

    print "{:.1f}".format(mf.median)
