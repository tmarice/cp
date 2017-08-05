


def main():
    g = int(raw_input())
    for _ in range(g):
        n = int(raw_input())
        xs = [(int(x), i) for i, x in enumerate(raw_input().split())]

        xs.sort(reverse=True)

        out = 0
        i = 0
        orig_pos =xs[0][1]

        # 1 5 2 3 4
        # (5, 1), (4, 4), (3, 3), (2, 2), (1, 0)

        while orig_pos != 0:

            j = i + 1
            while j < n and xs[j][1] > xs[i][1]:
                j += 1

            i = j
            orig_pos = xs[i][1]
            out = not out

        if out:
            print "ANDY"
        else:
            print "BOB"


main()
