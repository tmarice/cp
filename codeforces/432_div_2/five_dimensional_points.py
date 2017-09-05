
from collections import defaultdict
from math import acos, sqrt


EPS = 10 ** -8

def less_than(a, b):
    return b - a > EPS


def dot(pa, pb):
    return sum(pa[i] * pb[i] for i in range(5))


def angle(x, y):
    try:
        return acos(dot(x, y) / sqrt(dot(x, x) * dot(y, y)))
    except:
        return 90.0


def vector(pa, pb):
    return [b-a for a, b in zip(pa, pb)]


def origin_angles(v):
    return [


def main():
    n = int(input())
    acute = {i: set() for i in range(n)}

    points = [[int(x) for x in input().split()] for _ in range(n)]
    output = []

    for i in range(n):
        vectors = [vector(i, j) for j in range(n) if j != i]
        vectors.sort(key=origin_angle)

        bad_point = False
        for i in range(n-1):
            if less_than(angle(vectors[i], vectors[i + 1]), 90.0):
                bad_point = True
                break

        if not bad_point:
            output.append(i)

    print(len(output))

    for i in sorted(output):
        print(i + 1)


if __name__ == "__main__":
    main()
