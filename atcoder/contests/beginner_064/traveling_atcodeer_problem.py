


def main():
    n = int(raw_input())
    xs = [int(x) for x in raw_input().split()]

    xs.sort()

    print xs[-1] - xs[0]


main()


