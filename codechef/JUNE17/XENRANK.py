


def rank(x, y):
    r = 1

    r += y * (y+1) / 2
    xd = y + 2

    r += (x + xd - 1) * (x + xd) / 2 - xd * (xd - 1) / 2

    return r



def main():
    t = int(raw_input())

    for _ in range(t):
        u, v = [int(x) for x in raw_input().split()]

        print rank(u, v)


main()
