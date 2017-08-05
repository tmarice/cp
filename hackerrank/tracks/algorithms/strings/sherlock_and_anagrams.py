
from collections import defaultdict


def get_letters(s):
    r = [0] * 26

    for c in s:
        r[ord(c) - ord('a')] += 1

    return tuple(r)



t = int(raw_input())

for _ in range(t):
    s = raw_input()
    n = len(s)
    ss = defaultdict(int)

    for i in range(n):
        for j in range(i+1, n+1):
            letters = get_letters(s[i:j])
            ss[letters] += 1

    res = 0
    for l, c in ss.iteritems():
        res += c * (c-1) / 2

    print res
