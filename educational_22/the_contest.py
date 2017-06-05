




def main():
    n = int(raw_input())
    t = sum(int(x) for x in raw_input().split())
    m = int(raw_input())

    out = -1
    for _ in range(m):
        l, r = [int(x) for x in raw_input().split()]

        if out == -1 and t <= r:
            out = max(l, t)

    print out


main()


