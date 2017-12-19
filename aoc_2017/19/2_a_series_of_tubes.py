
import sys


DS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def simulate(graph, row, col):
    direction = (1, 0)
    steps = 1

    while True:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if graph[new_row][new_col] == "+":
            for dr, dc in DS:
                if new_row + dr != row and new_col + dc != col:
                    if graph[new_row + dr][new_col + dc] != " ":
                        direction = (dr, dc)
                        break
        elif graph[new_row][new_col] == " ":
            break

        row, col = new_row, new_col
        steps += 1

    return steps


def main():
    graph = sys.stdin.readlines()

    for i, c in enumerate(graph[0]):
        if c == "|":
            break

    steps = simulate(graph, 0, i)
    print(steps)


if __name__ == "__main__":
    main()
