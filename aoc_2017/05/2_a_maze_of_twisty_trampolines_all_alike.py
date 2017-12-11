
import sys


def simulate(l):
    steps = 0
    index = 0
    end = len(l)

    while 0 <= index < end:
        n_index = index + l[index]

        if l[index] >= 3:
            l[index] -= 1
        else:
            l[index] += 1

        index = n_index
        steps += 1

    return steps


def main():
    l = []
    for line in sys.stdin:
        l.append(int(line.strip()))

    steps = simulate(l)
    print(steps)


if __name__ == "__main__":
    main()
