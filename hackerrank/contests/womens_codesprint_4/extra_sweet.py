

def main():
    n, s = (int(x) for x in input().split())

    left = {0: 0}
    right = {n-1: 0}

    for _ in range(s):
        l, r = (int(x) for x in input().split())

        t = int(r * (r + 1) // 2 - l * (l - 1) // 2)

        ll = left.get(l, l - 1)
        rr = right.get(r, r + 1)

        lll = left.get(ll, ll - 1)
        rrr = right.get(rr, rr + 1)

        left[rrr] = lll
        right[lll] = rrr

        t += ll + rr

        print(t)


if __name__ == "__main__":
    main()
