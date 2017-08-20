
from collections import deque


MOD = 10 ** 9 + 7

def main():
    n = int(input())
    ds = [input(), input()]

    total = 1
    i = 0

    while i < n:
        if ds[0][i] == ds[1][i]: # vertical segment
            if i == 0: # first element, 3 colors
                x = 3
            else:
                if ds[0][i - 1] == ds[1][i - 1]: # previous segment vertical, 2 colors
                    x = 2
                else:
                    x = 1
        else: # horizontal segment
            if i == 0: # first element, 3 * 2 = 6 colorings
                x = 6 
            else:
                if ds[0][i - 1] == ds[1][i - 1]: # previous segment vertical, 2 colors
                    x = 2
                else:
                    x = 3

            i += 1

        total = (total * x) % MOD

        i += 1

    print(total)


if __name__ == "__main__":
    main()
