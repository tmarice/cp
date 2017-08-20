
from collections import defaultdict


def main():
    n = int(input())
    xs = [int(x) for x in input().split()]

    lens = defaultdict(int)

    for x in xs:
        lens[x] += 1

    max_a = 0
    max_b = 0

    sides = sorted(
        [(length, num) for length, num in lens.items() if num >= 2],
        reverse=True,
    )

    if len(sides) >= 1 and sides[0][1] >= 4:
        max_a = sides[0][0]
        max_b = max_a
    elif len(sides) >= 2:
        max_a = sides[0][0]
        max_b = sides[1][0]

    print(max_a * max_b)


if __name__ == "__main__":
    main()


