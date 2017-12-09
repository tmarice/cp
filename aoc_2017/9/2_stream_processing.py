
import sys


def main():
    score = 0
    garbage = False
    ignore = False

    for c in sys.stdin.readline():
        if garbage:
            if ignore:
                ignore = False
            elif c == '!':
                ignore = True
            elif c == '>':
                garbage = False
            else:
                score += 1

        else:
            if c == '<':
                garbage = True

    print(score)


if __name__ == "__main__":
    main()
