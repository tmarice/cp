


def main():
    n, k, t = (int(x) for x in input().split())

    if t <= k:
        print(t)
    elif t >= n:
        print(k-t+n)
    else:
        print(k)


if __name__ == "__main__":
    main()

