
from collections import defaultdict


memo = {}
graph = defaultdict(list)
burnout = []

n = 0


def solve(node, parent, parent_sent):
    if len(graph[node]) == 0:
        if parent_sent:
            return 0
        else:
            return burnout[node]

    if (node, parent_sent) in memo:
        return memo[(node, parent_sent)]

    # if parent burned out and not sent



def main():
    global n, burnout, graph

    n = int(raw_input())

for node in range(n):
    parent, happy = [int(x) for x in raw_input().split()]

    graph[parent].append(node)
    burnout.append(1 if happy == 0 else 1)

print solve(0, False)


if __name__ == "__main__":
    main()
