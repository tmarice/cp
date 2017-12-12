
import sys


def search(graph):
    visited = [False] * (max(graph) + 1)

    s = [0]
    visited[0] = True
    count = 0

    while s:
        cur = s.pop()
        count += 1

        for neighbor in graph[cur]:
            if not visited[neighbor]:
                visited[neighbor] = True
                s.append(neighbor)

    return count


def main():
    graph = {}

    for line in sys.stdin:
        a, b = line.split(" <-> ")
        bs = [int(x) for x in b.split(", ")]

        graph[int(a)] = bs


    o = search(graph)
    
    print(o)



if __name__ == "__main__":
    main()
