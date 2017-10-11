

INF = 10 ** 9 + 7


def main():
    exec("arr, (a, b) = " + input(), globals(), globals())

    positions = []

    for i, x in enumerate(arr):
        if x == a:
            positions.append((i, 0))
        elif x == b:
            positions.append((i, 1))

    min_dist = INF

    positions.sort()
    n = len(positions)

    for i in range(n - 1):
        if positions[i][1] != positions[i + 1][1]:
            min_dist = min(min_dist, abs(positions[i][0] - positions[i + 1][0]))

    print(min_dist)


if __name__ == "__main__":
    main()
