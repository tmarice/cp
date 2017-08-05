

def calculate(cx, xs, vs):
    ts = [(abs(x-cx) / v, i) for i, (x, v) in enumerate(zip(xs, vs))]
    ts.sort()

    if len(ts) > 1:
        if ts[0][0] == ts[1][0]:
            return -1

    return ts[0][1]


def main():
    n, x = [int(a) for a in raw_input().split()]
    xs = [int(a) for a in raw_input().split()]
    vs = [int(a) for a in raw_input().split()]

    print calculate(x, xs, vs)


main()
