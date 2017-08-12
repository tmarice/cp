
from math import ceil


def check(xs, ones, twos, fours):
    for i in range(len(xs)):
        take_fours = min(xs[i] // 4, fours)
        fours -= take_fours
        xs[i] -= take_fours * 4

        take_threes = min(xs[i] // 3, fours)
        fours -= take_threes
        xs[i] -= take_threes * 3

        take_twos = min(xs[i] // 2, twos)
        twos -= take_twos
        xs[i] -= take_twos * 2

        if xs[i] == 1:
            if ones:
                ones -= 1
                xs[i] = 0
            elif twos:
                twos -= 1
                xs[i] = 0

    return all(x == 0 for x in xs)


def main():
    n, k = (int(x) for x in input().split())
    xs = [int(x) for x in input().split()]
    xs.sort(reverse=True)

    for i in range(n+1):
        if check(list(xs), i, n * 2 + i, n - i):
            print("YES")
            break
    else:
        print("NO")


if __name__ == "__main__":
    main()
