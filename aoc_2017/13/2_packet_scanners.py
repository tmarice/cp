
import sys


def get_delay(depths):

    for delay in range(10000000):
        caught = False
        for time, depth in enumerate(depths):
            if depth == 0:
                continue

            if (delay + time) % (2 * depth - 2) == 0:
                caught = True
                break

        if not caught:
            return delay


def main():
    depths = [0] * 100

    for line in sys.stdin:
        layer, depth = (int(x) for x in line.split(": "))
        depths[layer] = depth

    d = get_delay(depths)
    print(d)


if __name__ == "__main__":
    main()
