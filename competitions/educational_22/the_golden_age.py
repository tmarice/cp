

def main():
    x, y, l, r = [int(x) for x in raw_input().split()]

    h = set()

    f = min(x, y)
    s = max(x, y)

    for i in range(60):
        for j in range(60):
            t = s ** i + f ** j
            h.add(t)

    lt = sorted(h)
    check = []

    for x in lt:
        if x >= l and x <= r:
            check.append(x)

    if len(check) == 0:
        out = r - l + 1
    elif len(check) == 1:
        out = max(check[0] - l, r - check[0])
    else:
        out = 0
        for i in range(len(check)):
            if i == 0:
                d = check[i] - l
            elif i == len(check) - 1:
                d = r - check[i]
            else:
                d = check[i+1] - check[i] - 1

            out = max(out, d)

    print out

main()
