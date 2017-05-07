


memo = {}


def dp(i, rs):
    if i in memo:
        return memo[i]

    if i == 0:
        if rs[i] <= rs[i+1]:
            memo[i] = 1
        else:
            memo[i] = dp(i+1, rs) + 1
    elif i == len(rs) - 1:
        if rs[i] <= rs[i-1]:
            memo[i] = 1
        else:
            memo[i] = dp(i-1, rs) + 1
    else:
        if rs[i] > rs[i-1] and rs[i] > rs[i+1]:
            memo[i] = max(dp(i-1, rs), dp(i+1, rs)) + 1
        elif rs[i] > rs[i-1]:
            memo[i] = dp(i-1, rs) + 1
        elif rs[i] > rs[i+1]:
            memo[i] = dp(i+1, rs) + 1
        else:
            memo[i] = 1

    return memo[i]




def main():
    n = int(raw_input())
    rs = []

    for _ in range(n):
        rs.append(int(raw_input()))

    s = 0
    for i in range(n):
        s += dp(i, rs)

    print s


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(1<<20)
    main()

