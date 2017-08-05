

MAX_N = 3001
MOD = 10 ** 9 + 7

m = [[0] * MAX_N for _ in range(MAX_N)]


def precompute():
    m[0][1] = 1

    for i in xrange(1, MAX_N):
        diag = 2
        hor = i + 1

        for j in xrange(i+1, MAX_N):
            if hor == 0 and diag == 0:
                break
            else:
                r = ((hor * m[i][j-1]) % MOD + (diag * m[i-1][j-1]) % MOD) % MOD
                # r = hor * m[i][j-1] + diag * m[i-1][j-1]
                m[i][j] = r

                hor -= 1
                diag += 2

    for i in xrange(MAX_N-1, 0, -1):
        cumsum = 0

        for j in xrange(MAX_N-1, -1, -1):
            cumsum += m[j][i]
            cumsum %= MOD
            m[j][i] = cumsum



def main():
    precompute()

    # for i in range(10):
    #     for j in range(10):
    #         print m[i][j],
    #     print

    q = int(raw_input())

    for _ in range(q):
        n, k = [int(x) for x in raw_input().split()]

        print m[k][n]


if __name__ == "__main__":
    main()
