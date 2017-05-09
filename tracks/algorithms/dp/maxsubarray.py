

INF = 10 ** 9

def max_cont(xs):
    s = xs[0]
    ret = s 

    for x in xs[1:]:
        s = max(s + x, x)
        ret = max(ret, s)

    return ret


def max_noncont(xs):
    ret = xs[0]
    for i in range(1, len(xs)):
        cur = max(xs[i], ret + xs[i])
        ret = max(ret, cur)

    return ret


def main():
    t = int(raw_input())

    for _ in range(t):
        n = int(raw_input())
        xs = [int(x) for x in raw_input().split()]

        print max_cont(xs), max_noncont(xs)


if __name__ == "__main__":
    main()
