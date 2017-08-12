
from functools import reduce


def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    n = int(input())

    ts = []
    for _ in range(n):
        ts.append(int(input()))

    print(reduce(lcm, ts))


if __name__ == "__main__":
    main()

