import sys


def is_square(a, b, c, d):
    return a == b == c == d


def is_rectangle(a, b, c, d):
    return a == c and b == d 


def main():
    squares = 0
    rectangles = 0
    other = 0

    for l in sys.stdin:
        a, b, c, d = [int(x) for x in l.split(' ')]

        if any(x <= 0 for x in [a,b,c,d]):
            other += 1
        elif is_square(a,b,c,d):
            squares += 1
        elif is_rectangle(a, b, c, d):
            rectangles += 1
        else:
            other += 1

    print squares, rectangles, other


if __name__ == "__main__":
    main()
