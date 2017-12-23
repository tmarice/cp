
import sys

N = 18

def rotate(pattern):
    pattern = pattern.split("/")
    n = len(pattern[0])

    output_pattern = [list(l) for l in pattern]

    for i in range(n):
        for j in range(n):
            output_pattern[j][n-i-1] = pattern[i][j]

    return "/".join(("".join(s) for s in output_pattern))


def flip(pattern):
    pattern = pattern.split("/")
    n = len(pattern[0])

    output_pattern = [reversed(l) for l in pattern]

    return "/".join(("".join(s) for s in output_pattern))


def transform(pattern, n, transformations):
    l = len(pattern)

    upsize = 3 if n == 2 else 4
    output_pattern = ["" for _ in range(int(l/n*upsize))]

    for i in range(int(l/n)):
        for j in range(int(l/n)):
            mp = "/".join(s[j * n:(j + 1) * n] for s in pattern[i*n:(i+1) * n])
            tmp = transformations[mp]
            tmp = tmp.split("/")

            for k in range(len(tmp)):
                output_pattern[i*upsize + k] += tmp[k]

    return output_pattern


def solve(n, transformations):
    pattern = [
        ".#.",
        "..#",
        "###",
    ]

    for _ in range(n):
        if len(pattern[0]) % 2 == 0:
            pattern = transform(pattern, 2, transformations)
        elif len(pattern[0]) % 3 == 0:
            pattern = transform(pattern, 3, transformations)

    return pattern


def main():
    transformations = {}

    for line in sys.stdin:
        left, right = line.strip().split(" => ")

        transformations[left] = right
        transformations[flip(left)] = right

        transformations[rotate(left)] = right
        transformations[flip(rotate(left))] = right

        transformations[rotate(rotate(left))] = right
        transformations[flip(rotate(rotate(left)))] = right

        transformations[rotate(rotate(rotate(left)))] = right
        transformations[flip(rotate(rotate(rotate(left))))] = right

    pattern = solve(N, transformations)
    set_count = sum(1 for line in pattern for c in line if c == "#")

    print(set_count)


if __name__ == "__main__":
    main()
