

def main():
    x, y, l, r = [int(x) for x in raw_input().split()]

    h = set()

    f = min(x, y)
    s = max(x, y)

    for i in range(60):
        for j in range(60):
            t = x ** i + y ** j
            if t > r:
                break
            elif t >= l:
                h.add(t)


    lt = sorted(h)

    out = 0
    for i in range(len(lt)):
        if i == 0:
            d = lt[i] - l
        elif i == len(lt) - 1:
            d = r - lt[i]
        else:
            d = lt[i+1] - lt[i] - 1

        out = max(out, d)

    print out

main()
