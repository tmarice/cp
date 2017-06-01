


def solve(n, houses):
    ret = 1 if "*" in houses[0] and "*" in houses[1] else 0

    n_first = 0
    n_second = 0

    for i in range(n):
        f_inc = False
        s_inc = False

        if houses[0][i] == "*":
            n_first += 1
            f_inc = True

        if houses[1][i] == "*":
            n_second += 1
            s_inc = True

        if n_first > 1 or n_second > 1:
            ret += 1

            if n_first == 2 or not f_inc:
                n_first = max(n_first-1, 0)
            if n_second == 2 or not s_inc:
                n_second = max(n_second-1, 0)

    return ret


def main():
    t = int(raw_input())

    for _ in range(t):
        n = int(raw_input())

        houses = [raw_input() for _ in range(2)]

        print solve(n, houses)


main()
