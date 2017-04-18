
def rounded_grades(grades):
    ret = []

    for g in grades:
        if g < 38:
            ret.append(g)
        elif (g + 1) % 5 == 0:
            ret.append(g + 1)
        elif (g + 2) % 5 == 0:
            ret.append(g + 2)
        else:
            ret.append(g)

    return ret


def main():
    n = int(raw_input())
    grades = []

    for _ in range(n):
        grades.append(int(raw_input()))

    for rg in rounded_grades(grades):
        print rg


if __name__ == "__main__":
    main()

