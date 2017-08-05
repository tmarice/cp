def find_x(n, p):
    ret = []

    for x in range(n):
        for y in range(n):
            if p[p[y]-1] == x+1:
                ret.append(y+1)
                break

    return ret


def main():
    n = int(raw_input())

    p = [int(x) for x in raw_input().split()]

    ret = find_x(n, p)

    for r in ret:
        print r


if __name__ == "__main__":
    main()
