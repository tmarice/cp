


conds = (
    [lambda x: x <= 399, False],
    [lambda x: x <= 799, False],
    [lambda x: x <= 1199, False],
    [lambda x: x <= 1599, False],
    [lambda x: x <= 1999, False],
    [lambda x: x <= 2399, False],
    [lambda x: x <= 2799, False],
    [lambda x: x <= 3199, False],
)


def main():
    n = int(raw_input())
    xs = [int(x) for x in raw_input().split()]

    others = 0
    for x in xs:
        for cond in conds:
            if cond[0](x):
                cond[1] = True
                break
        else:
            others += 1

    s = sum(1 for c, t in conds if t)

    print s if s else 1,
    print s + others


main()
