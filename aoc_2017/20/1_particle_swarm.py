
import sys

INF = 10 ** 9 + 7


def md(x):
    return sum(abs(c) for c in x)


def main():
    points = []

    for i, line in enumerate(sys.stdin):
        p, v, a = line.strip().split(", ")

        p = [int(x) for x in p[3:-1].split(",")]
        v = [int(x) for x in v[3:-1].split(",")]
        a = [int(x) for x in a[3:-1].split(",")]

        points.append((md(a), md(v), md(p), i))

    points.sort()

    print(points[0][-1])


if __name__ == "__main__":
    main()
