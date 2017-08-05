

def main():
    n, m = [int(x) for x in raw_input().split()]

    l = [0] * (n+1)

    for _ in range(m):
        a, b, k = [int(x) for x in raw_input().split()]
        l[a-1] += k
        l[b] -= k

    m = 0
    cur = 0

    for x in l:
        cur += x
        m = max(m, cur)

    print m


if __name__ == "__main__":
    main()

