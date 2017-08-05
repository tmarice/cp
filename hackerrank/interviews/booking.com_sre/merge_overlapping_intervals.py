

def merge_overlapping_intervals():
    n = int(raw_input())
    diffs = []

    for _ in range(n):
        start, end = [int(x) for x in raw_input().split()]

        diffs.append((start, -1))
        diffs.append((end, 1))

    ints = []
    start = None
    cursum = 0

    for t, d in sorted(diffs):
        if cursum == 0 and d == -1:
            start = t

        if cursum == 1 and d == 1:
            ints.append((start, t))
            start = None

        cursum -= d

    print len(ints)
    for start, end in ints:
        print start, end


merge_overlapping_intervals()
