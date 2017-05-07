


def convert(s):
    h = int(s[:2])
    m = int(s[3:5])
    t = s[5]

    if t == 'A' and h == 12:
        h -= 12

    if t == 'P' and h != 12:
        h += 12

    return h * 60 + m


def main():
    q = int(raw_input())

    for _ in range(q):
        t1, t2 = [convert(x) for x in raw_input().split()]

        print "First" if t1 < t2 else "Second"


if __name__ == "__main__":
    main()
