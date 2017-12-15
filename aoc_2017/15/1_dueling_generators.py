


A_FACTOR = 16807
B_FACTOR = 48271
MOD = 2147483647
MASK = 2 ** 16 - 1

N = 40000000


def lower_16(a, b):
    for _ in range(16):
        if (a ^ b) & MASK != 0:
            return False

    return True


def count(a, b):
    result = 0

    for i in range(N):
        a = (a * A_FACTOR) % MOD
        b = (b * B_FACTOR) % MOD

        if lower_16(a, b):
            result += 1

        if i % 1000 == 0:
            print(i)

    return result


def main():
    a_start = int(input().strip().split()[-1])
    b_start = int(input().strip().split()[-1])

    r = count(a_start, b_start)

    print(r)


if __name__ == "__main__":
    main()
