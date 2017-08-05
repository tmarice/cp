

def diff(n, xs):
    mid = n / 2
    left_sum = 0
    right_sum = 0

    for i, x in enumerate(xs):
        if i < mid:
            left_sum += x
        else:
            right_sum += x

    return abs(left_sum - right_sum)


def main():
    n = int(raw_input())
    xs = [int(x) for x in raw_input().split()]

    print diff(n, xs)


main()
