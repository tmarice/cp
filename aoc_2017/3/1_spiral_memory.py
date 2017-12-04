
DIFFS = ((1, 0), (0, -1), (-1, 0), (0, 1))

def get_coords(n):
    coords = [0, 0]
    steps = 1
    direction = 0
    i = 1

    while True:
        for _ in range(2):
            for _ in range(steps):
                if i == n:
                    return coords

                coords[0] += DIFFS[direction][0]
                coords[1] += DIFFS[direction][1]

                i += 1
            direction = (direction + 1) % 4
        steps += 1


def distance(x, y):
    return abs(x[0]  - y[0]) + abs(x[1] - y[1])


def main():
    n = int(input())

    coords = get_coords(n)
    d = distance((0, 0), coords)
    print(d)


if __name__ == "__main__":
    main()
