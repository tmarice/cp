

def valid(hs, n):
    first = hs[:n/2]
    half = hs[n/2]
    second = hs[n/2+1:]

    return (first == range(1, n/2+1) and
           half == first[-1] + 1 and
           half == second[0] + 1 and
           second == list(reversed(range(1, n/2+1))))


def main():
    s = int(raw_input())

    for _ in range(s):
        n = int(raw_input())
        hs = [int(x) for x in raw_input().split()]

        print "yes" if valid(hs, n) else "no"


if __name__ == "__main__":
    main()
