


def solve(n, houses):
    n_first = sum(1 for c in houses[0] if c == "*")
    n_second = sum(1 for c in houses[1] if c == "*")

    ret = 1 if n_first and n_second else 0

    for i in range(n):
        if n_first <= 1 and n_second <= 1:
            break
        if houses[0][i] == "*" and houses[1][i] == "*":
            ret += 1
            n_first -= 1
            n_second -= 1
        elif houses[0][i] == "*":
            ret += 1
            n_first -= 1
        elif houses[1][i] == "*":
            ret += 1
            n_second -= 1

    return ret


def main():
    t = int(raw_input())

    for _ in range(t):
        n = int(raw_input())

        houses = [raw_input() for _ in range(2)]

        print solve(n, houses)


main()
