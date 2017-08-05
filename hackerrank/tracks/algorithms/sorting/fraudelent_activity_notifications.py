
from collections import deque


class MedianTracker(object):

    def __init__(self, xs):
        if len(xs) % 2 == 1:
            self._target = [len(xs) / 2 + 1]
        else:
            self._target = [len(xs)/2, len(xs)/2+1]

        self._hist = [0] * 201
        self._q = deque(xs)

        for x in xs:
            self._hist[x] += 1


    def push(self, x):
        self._hist[self._q.popleft()] -= 1
        self._q.append(x)
        self._hist[x] += 1


    @property
    def median(self):
        sum = 0
        n = 0

        for t in self._target:
            cumsum = 0

            for i in range(201):
                cumsum += self._hist[i]

                if cumsum >= t:
                    sum += i
                    n += 1
                    break

        return float(sum) / n


n, d = [int(x) for x in raw_input().split()]
exs = [int(x) for x in raw_input().split()]

mt = MedianTracker(exs[:d])
count = 0

for ex in exs[d:]:
    if ex >= 2 * mt.median:
        count += 1

    mt.push(ex)

print count
