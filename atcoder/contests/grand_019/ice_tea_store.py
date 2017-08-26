

def main():
    q, h, s, d = (int(x) for x in input().split())
    n = int(input())

    one_l = min(q * 4, h * 2, s)
    two_l = d

    if two_l / 2 < one_l:
        cost = (n // 2) * two_l + (n % 2) * one_l
    else:
        cost = n * one_l

    print(cost)


if __name__ == "__main__":
    main()

