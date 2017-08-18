

memo = {}
prices = []


def dp(start, n_trans):
    if (start, n_trans) in memo:
        return memo[(start, n_trans)]

    if start >= len(prices) - 1:
        return 0

    if n_trans == 0:
        return 0

    output = 0
    for start_tent in range(start, len(prices)):
        for end in range(start_tent + 1, len(prices)):
            profit = prices[end] - prices[start_tent] + dp(end, n_trans - 1)

            if profit > output:
                output = profit

    memo[(start, n_trans)] = output
    return output


def main():
    global memo, prices
    q = int(input())

    for _ in range(q):
        k = int(input())
        n = int(input())
        prices = [int(x) for x in input().split()]
        memo = {}

        print(dp(0, k))


if __name__ == "__main__":
    main()
