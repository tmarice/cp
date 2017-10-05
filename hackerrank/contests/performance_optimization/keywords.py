
from collections import deque

MAX = 1000000007


def bs(words, keys, buf_len):
    buf = deque()
    min_len = MAX

    for w in words:
        if len(buf) < buf_len:
            buf.appendleft(w)
        else:
            buf.pop()
            buf.appendleft(w)

            if keys.issubset(set(buf)):
                min_len = min(min_len, sum(len(x) for x in buf) + buf_len - 1)

    if keys.issubset(set(buf)):
        min_len = min(min_len, sum(len(x) for x in buf) + buf_len - 1)

    return min_len


def minimumLength(text, keys):
    keys = set(keys)
    n = len(keys)
    words = text.split()

    lo = 0
    hi = len(words)

    out = bs(words, keys, hi)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        r = bs(words, keys, mid)

        if r != MAX:
            out = min(out, r)
            hi = mid
        else:
            lo = mid + 1

    return -1 if out == MAX else out


text = input()
keywords = int(input())
keys = []
for _ in range(keywords):
    keys.append(input())

print(minimumLength(text, keys))


