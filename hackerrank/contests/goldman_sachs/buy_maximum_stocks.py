


def main():
    n = int(input())
    prices = ((int(x), i+1) for i, x in enumerate(input().split()))
    k = int(input())

    total = 0

    for p, max_s in sorted(prices):
        m = p * max_s

        if m <= k:
            total += max_s
            k -= m
        else:
            total += k // p
            break

    print(total)


if __name__ == "__main__":
    main()

