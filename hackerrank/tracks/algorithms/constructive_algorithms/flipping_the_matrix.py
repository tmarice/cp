

def solve(m, n):
    ret = 0
    for i in range(n):
        for j in range(n):
            ret += max(
                    m[i][j],
                    m[2*n-i-1][j],
                    m[i][2*n-j-1],
                    m[2*n-i-1][2*n-j-1],
            )

    return ret


def main():
    q = int(raw_input())
    for _ in range(q):
        n = int(raw_input())

        m = []
        for _ in range(2*n):
            m.append([int(x) for x in raw_input().split()])

        print solve(m, n)


if __name__ == "__main__":
    main()
