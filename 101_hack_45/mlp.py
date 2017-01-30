def calc(n, k):
    if n < k:
        return -1

    if k > 2:
        return (n-k+1)*2 + k - 3
    else:
        if n == 2:
            return 1
        else:
            return -1


def main():
    n, k = [int(x) for x in raw_input().split()]

    print calc(n, k)


if __name__ == "__main__":
    main()
