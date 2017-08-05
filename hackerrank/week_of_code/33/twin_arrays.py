

INF = 1000000000


def main():
    n = int(raw_input())
    xs = [(int(x), i) for i, x in enumerate(raw_input().split())]
    ys = [(int(x), i) for i, x in enumerate(raw_input().split())]

    m = INF
    i = 0
    j = 0

    xs.sort()
    ys.sort()

    while i < len(xs) and j < len(ys):
        if xs[i][1] != ys[j][1]:
            m = xs[i][0] + ys[j][0]
            break
        else:
            if i+1 < len(xs) and j+1 < len(ys) and xs[i+1][0] < ys[j+1][0]:
                i += 1
            elif i+1 < len(xs) and j+1 < len(ys) and xs[i+1][0] >= ys[j+1][0]:
                j += 1
            else:
                break

    print m

main()


