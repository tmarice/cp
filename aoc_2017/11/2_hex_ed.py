
MOVES = {
    "n": (0, 1, -1),
    "ne": (1, 0, -1),
    "se": (1, -1, 0),
    "s": (0, -1, 1),
    "sw": (-1, 0, 1),
    "nw": (-1, 1, 0),
}


def trace(steps):
    end =[0, 0, 0]
    furthest = 0

    for step in steps:
        dx, dy, dz = MOVES[step]

        end[0] += dx
        end[1] += dy
        end[2] += dz

        d = max(abs(x) for x in end)
        furthest = max(furthest, d)
    
    return furthest


def main():
    steps = input().strip().split(",")

    n_s = trace(steps)
    print(n_s)


if __name__ == "__main__":
    main()
