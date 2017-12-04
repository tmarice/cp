
from collections import defaultdict


DIFFS = ((1, 0), (0, -1), (-1, 0), (0, 1))
DS = ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1))

def get_limit(limit):
    memo = defaultdict(int)
    memo[(0, 0)] = 1

    coords = [0, 0]
    steps = 1
    direction = 0
    i = 1

    while True:
        for _ in range(2):
            for _ in range(steps):
                coords[0] += DIFFS[direction][0]
                coords[1] += DIFFS[direction][1]

                cur_sum = 0
                for dx, dy in DS:
                    cur_sum += memo[(coords[0] + dx, coords[1] + dy)]

                if cur_sum > limit:
                    return cur_sum
                else:
                    memo[(coords[0], coords[1])] = cur_sum


                i += 1
            direction = (direction + 1) % 4
        steps += 1


def main():
    n = int(input())

    l = get_limit(n)
    print(l)


if __name__ == "__main__":
    main()
