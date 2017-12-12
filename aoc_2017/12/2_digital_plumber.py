
import sys


def search(graph):
    n = max(graph) + 1
    visited = [False] * n

    count = 0

    for i in range(n):
        if not visited[i]:
            s = [i]
            visited[i] = True
            count += 1

            while s:
                cur = s.pop()

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
