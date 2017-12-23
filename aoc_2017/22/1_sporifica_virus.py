
import sys


N = 10000
DS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def simulate(graph, N):
    output = 0
    direction = 0
    x = 0
    y = 0

    for _ in range(N):
        if (y, x) in graph:
            direction = (direction + 1) % 4
            graph.remove((y, x))
        else:
            direction = (direction - 1) % 4
            graph.add((y, x))
            output += 1

        y += DS[direction][0]
        x += DS[direction][1]

    return output


def main():
    graph_in = [s.strip() for s in sys.stdin]

    n = len(graph_in)
    m = len(graph_in[0])

    cx = m / 2
    cy = n / 2

    graph = set()
    for i in range(-cy, cy+1):
        for j in range(-cx, cx+1):
            if graph_in[i+cy][j+cx] == "#":
                graph.add((i, j))

    infected = simulate(graph, N)
    print(infected)


if __name__ == "__main__":
    main()
