


def main():
    n, m, k = (int(x) for x in input().split())
    dollar_price = [int(x) for x in input().split()]
    btc_price = [int(x) for x in input().split()]

    out = max(m * x * y for x, y in zip(dollar_price, btc_price))
    out = max(out, m * k)

    print(out)


if __name__ == "__main__":
    main()



