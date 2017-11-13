

def validate_price(price):
    n7 = 0
    n4 = 0

    for c in price:
        if c == '7':
            n7 += 1
        elif c == '4':
            n4 += 1
        else:
            return False

    return n7 == n4


def main():
    n = int(input())
    candidates = []

    for _ in range(n):
        name, price = input().split()

        if validate_price(price):
            candidates.append((int(price), name))

    if candidates:
        print(min(candidates)[1])
    else:
        print(-1)


if __name__ == "__main__":
    main()
