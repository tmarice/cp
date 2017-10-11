
from math import fabs


EPS = 1e-6


def area(x1, y1, x2, y2, x3, y3):
    return (
        x1 * (y2 - y3) +
        x2 * (y3 - y1) +
        x3 * (y1 - y2)) / 2


def main():
    t = int(input())

    for _ in range(t):
        x1, y1, x2, y2, x3, y3 = (int(x) for x in input().split("\t"))

        if fabs(area(x1, y1, x2, y2, x3, y3)) <= EPS:
            print("YES")
        else:
            print("NO")

main()
