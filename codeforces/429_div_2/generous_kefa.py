
from collections import defaultdict


def main():
    n, k = (int(x) for x in input().split())
    s = input()
    d = defaultdict(int)

    for c in s:
        d[c] += 1
        if d[c] > k:
            print("NO")
            break
    else:
        print("YES")


if __name__ == "__main__":
    main()
