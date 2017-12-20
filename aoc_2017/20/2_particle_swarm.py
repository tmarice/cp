
import sys
from collections import defaultdict

N = 10000

class Point():

    def __init__(self, p, v, a):
        self.p = p
        self._v = v
        self._a = a


    def tick(self):
        for i in range(3):
            self._v[i] += self._a[i]

        for i in range(3):
            self.p[i] += self._v[i]


def main():
    points = []

    for i, line in enumerate(sys.stdin):
        p, v, a = line.strip().split(", ")

        p = [int(x) for x in p[3:-1].split(",")]
        v = [int(x) for x in v[3:-1].split(",")]
        a = [int(x) for x in a[3:-1].split(",")]

        points.append(Point(p, v, a))

    for i in range(N):
        pos = defaultdict(list)

        for point in points:
            point.tick()
            pos[tuple(point.p)].append(point)

        points = [p[0] for p in pos.values() if len(p) == 1]
        print(i)

    print(len(points))


if __name__ == "__main__":
    main()
