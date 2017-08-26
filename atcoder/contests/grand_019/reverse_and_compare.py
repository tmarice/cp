
from collections import defaultdict


def main():
    a = input()
    z = defaultdict(int)

    for c in a:
        z[c] += 1

    n = len(a)

    no_count = 0
    for k, v in z.items():
        no_count += v * (v - 1) // 2

    print(n * (n - 1) // 2 + 1 - no_count)


if __name__ == "__main__":
    main()




