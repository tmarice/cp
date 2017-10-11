

def solve(xs):
    suffix_sum = sum(xs)
    prefix_sum = 0

    l = len(xs)

    for i in range(0, l-1): #xs[i] last element in prefix
        prefix_sum += xs[i]
        suffix_sum -= xs[i]

        if prefix_sum == suffix_sum:
            return i + 1

    return 0


def main():
    n = int(input())

    for _ in range(n):
        xs = [int(x) for x in input().split()]
        print(solve(xs[1:]))


if __name__ == "__main__":
    main()
