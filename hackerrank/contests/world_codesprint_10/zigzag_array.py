

def min_remove(xs, n):
    if n < 3:
        return 0

    i = 0
    j = 1
    k = 2

    out = 0

    import pdb; pdb.set_trace()
    while i < j < k < n:
        if (xs[i] > xs[j] > xs[k] or
            xs[i] < xs[j] < xs[k]):
            out += 1

            j = k
            k += 1
        else:
            i = j
            j = k
            k += 1

    return out


def main():
    n = int(raw_input())
    xs = [int(x) for x in raw_input().split()]

    print min_remove(xs, n)


if __name__ == "__main__":
    main()
