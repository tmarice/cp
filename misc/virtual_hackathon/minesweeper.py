
import fileinput
from collections import defaultdict


dx = [0, 1, 1 ,1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def solve(n, m, field, cnt):
    if n == 0 and m == 0 and field == []:
        return

    adj = defaultdict(int)
    mines = set()

    for i, row in enumerate(field):
        for j, c in enumerate(row):
            if c == '*':
                mines.add((j, i))

                for dxx, dyy in zip(dx, dy):
                    adj[(j + dxx, i + dyy)] += 1
    
    print("Field #{0}".format(cnt))

    for i in range(n):
        for j in range(m):
            if (j, i) in mines:
                print("*", end="")
            else:
                print(adj[(j, i)], end="")
        print()

    print()


def main():
    cnt = 0
    next_target = 0
    n = -1
    m = -1
    field = []

    lines = fileinput.input()
    while n != 0 and m != 0:
        line = next(lines).strip()

        if line:

            field = []
            n, m = (int(x) for x in line.split())

            i = 0

            while i < n:
                line = next(lines).strip()

                if line:
                    field.append(line.strip())
                    i += 1

            solve(n, m, field, cnt)

            cnt += 1

main()
