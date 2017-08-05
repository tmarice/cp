

def main():
    x, y, l, r = [int(x) for x in raw_input().split()]

    h = set([l-1, r+1])
    LIMIT = 10 ** 18

    for i in range(60):
        a = x ** i
        if a > LIMIT:
            break

        for j in range(60):
            b = a + y ** j

            if b > LIMIT:
                break
            else:
                h.add(b)

    lt = sorted(h)
    check = []

    for x in lt:
        if x >= l-1 and x <= r+1:
            check.append(x)

    out = 0
    for i in range(1, len(check)):
        out = max(out, check[i] - check[i-1] - 1)

    print out

main()
