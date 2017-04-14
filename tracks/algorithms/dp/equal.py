
INF = 10 ** 9


def decompose(x):
    n_5 = x / 5
    x %= 5

    n_2 = x / 2
    x %= 2

    n_1 = x

    return n_1 + n_2 + n_5


t = int(raw_input())

for _ in range(t):
    n = int(raw_input())
    cs = [int(x) for x in raw_input().split()]
    m = min(cs)

    out = INF
    for base in range(0, 3):
        cur_out = 0

        for c in cs:
            d = c - m + base
            cur_out += decompose(d)

        out = min(out, cur_out)

    print out
