

def main():
    a, b, c, d = [int(x) for x in input().split()]

    xs = [0] * 101
    xs[a] += 1
    xs[b] -= 1
    xs[c] += 1
    xs[d] -= 1

    cursum = 0
    t = 0
    for x in xs:
        cursum += x
        if cursum == 2:
            t += 1

    print(t)


if __name__ == "__main__":
    main()
