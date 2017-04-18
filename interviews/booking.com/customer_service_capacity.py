from operator import itemgetter


def main():
    cur = int(raw_input())
    n = int(raw_input())

    points = []
    for _ in range(n):
        start, end = [int(x) for x in raw_input().split()]

        points.append((start, 1))
        points.append((end, -1))

    max_calls = 0
    cur_calls = 0

    for _, v in sorted(points, key=itemgetter(0)):
        cur_calls += v
        max_calls = max(max_calls, cur_calls)

    diff = max_calls - cur
    print 
    if diff > 0:
        print diff
    else:
        print 0


if __name__ == "__main__":
    main()
