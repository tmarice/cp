

from math import ceil


def solve(xs, n):
    moves = [0] * (n+1)
    out = 0

    for i in range(n):
        swapped = False
        for j in range(n-1):
            if xs[j] > xs[j+1]:
                moves[xs[j]] += 1
                if moves[xs[j]] > 2:
                    return "Too chaotic"
                xs[j], xs[j+1] = xs[j+1], xs[j]
                swapped = True
        if not swapped:
            break

    return sum(moves)


def main():
    t = int(raw_input())
    for _ in range(t):
        n = int(raw_input())
        xs = [int(x) for x in raw_input().split()]

        print solve(xs, n)

main()


