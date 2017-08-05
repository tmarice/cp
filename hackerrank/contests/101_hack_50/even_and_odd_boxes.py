
from itertools import izip


def calc(n, caps):
    orig_caps = list(caps)
    k = 0

    for i in range(n):
        if i % 2 == 0:
            if caps[i] % 2 == 1 and k == 1 or caps[i] == 1:
                caps[i] += 1
                k -= 1
            elif caps[i] % 2 == 1 and (k == 0 or k < 0):
                caps[i] -= 1
                k += 1
        else:
            if caps[i] % 2 == 0 and k == 1:
                caps[i] += 1
                k -= 1
            elif caps[i] % 2 == 0 and (k == 0 or k < 0):
                caps[i] -= 1
                k += 1

#    import pdb; pdb.set_trace()
    if k % 2 == 1:
        return -1

    if k < 0:
        for i in range(n):
            if i % 2 == 0 and caps[i] > 2:
                d = min(caps[i] - 2, k)
                caps[i] -= d
                k += d
            elif i % 2 == 1 and caps[i] > 1:
                d = min(caps[i] - 1, k)
                caps[i] -= d
                k += d


#    import pdb; pdb.set_trace()
#    print caps

    if k != 0:
        return -1
    else:
        return sum(abs(oc - c) for oc, c in izip(orig_caps, caps)) / 2


def main():
    t = int(raw_input())

    for _ in range(t):
        n = int(raw_input())
        caps = [int(x) for x in raw_input().split()]

        print calc(n, caps)


if __name__ == "__main__":
    main()
