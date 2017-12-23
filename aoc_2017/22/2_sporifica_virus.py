
import sys

N = 10000000
DS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def simulate(infected, N):
    weakened = set()
    flagged = set()
    output = 0
    direction = 0
    x = 0
    y = 0

    for i in range(N):
        if i % 1000 == 0:
            print(i)
        if (y, x) in infected:
            direction = (direction + 1) % 4
            infected.remove((y, x))
            flagged.add((y, x))
        elif (y, x) in weakened:
            weakened.remove((y, x))
            infected.add((y, x))
            output += 1
        elif (y, x) in flagged:
            flagged.remove((y, x))
            direction = (direction + 2) % 4
        else:
            direction = (direction - 1) % 4
            weakened.add((y, x))

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
