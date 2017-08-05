

from math import ceil


def main():
    n, hit, t = [int(x) for x in raw_input().split()]
    hs = [int(x) for x in raw_input().split()]

    k = 0
    for h in sorted(hs):
        b = int(ceil(h/float(hit)))

        if t - b >= 0:
            t -= b
            k += 1
        else:
            break

    print k

main()



