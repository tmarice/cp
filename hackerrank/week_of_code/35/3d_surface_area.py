


def main():
    r, c = (int(x) for x in input().split())

    hs = []

    for _ in range(r):
        hs.append([int(x) for x in input().split()])


    total = 0
    for i in range(r):
        for j in range(c):
            total += 4 * hs[i][j] + 2 
            if i > 0:
                total -= hs[i - 1][j] if hs[i - 1][j] < hs[i][j] else hs[i][j]
            if i < r - 1:
                total -= hs[i + 1][j] if hs[i + 1][j] < hs[i][j] else hs[i][j]
            if j > 0:
                total -= hs[i][j - 1] if hs[i][j - 1] < hs[i][j] else hs[i][j]
            if j < c - 1:
                total -= hs[i][j + 1] if hs[i][j + 1] < hs[i][j] else hs[i][j]

    print(total)


if __name__ == "__main__":
    main()
