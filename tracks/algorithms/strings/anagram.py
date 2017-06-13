

from collections import defaultdict


def count(s):
    if len(s) % 2 == 1:
        return -1

    s1 = s[:len(s)/2]
    s2 = s[len(s)/2:]

    c1 = defaultdict(int)
    c2 = defaultdict(int)

    for c in s1:
        c1[c] += 1

    for c in s2:
        c2[c] += 1

    out = 0
    for i in xrange(ord('a'), ord('z')+1):
        out += abs(c1[chr(i)] - c2[chr(i)])

    return out / 2


def main():
    t = int(raw_input())

    for _ in range(t):
        s = raw_input()
        print count(s)

main()
