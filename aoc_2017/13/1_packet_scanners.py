
import sys


def get_severity(depths):
    severity = 0

    n = len(depths)
    for time, depth in enumerate(depths):
        if time % (2 * depth - 2) == 0:
            severity += time * depth

    return severity


def main():
    depths = [0] * 100

    for line in sys.stdin:
        layer, depth = (int(x) for x in line.split(": "))
        depths[layer] = depth

    s = get_severity(depths)
    print(s)


if __name__ == "__main__":
    main()
