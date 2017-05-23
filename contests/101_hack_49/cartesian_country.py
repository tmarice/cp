
INF = 1000000000


def main():
    x1, y1 = [int(x) for x in raw_input().split()]
    x2, y2 = [int(x) for x in raw_input().split()]
    xc, yc = [int(x) for x in raw_input().split()]

    min_y = INF
    min_x = INF

    min_x = min(min_x, abs(x1 - xc))
    min_x = min(min_x, abs(x2 - xc))
    min_y = min(min_y, abs(y1 - yc))
    min_y = min(min_y, abs(y2 - yc))

    print ((2 * min_y + 1) * (2 * min_x + 1) - 1) / 2



main()


