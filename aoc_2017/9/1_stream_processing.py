
import sys


def main():
    outter = 0
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
            if c == '{':
                outter += 1
            elif c == '}':
                score += outter
                outter -= 1
            elif c == '<':
                garbage = True

    print(score)


if __name__ == "__main__":
    main()
