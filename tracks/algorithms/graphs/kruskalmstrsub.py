
import heapq
from functools import total_ordering


@total_ordering
class Edge(object):

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.r == other.r

    def __lt__(self, other):
        if self.r == other.r:
            return (self.x + self.r + self.y) < (other.x + other.r + other.y)
        else:
            return self.r < other.r

    def __str__(self):
        return "({0}, {1}) - {2}".format(self.x, self.y, self.r)

    def __repr__(self):
        return self.__str__()


n, m = [int(x) for x in raw_input().split()]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, r = [int(a) for a in raw_input().split()]
    graph[x].append(Edge(x, y, r))
    graph[y].append(Edge(x, y, r))


# use prim - easier because not disjoint set data structure
out = 0
visited = set([1])
h = []
for e in graph[1]:
    heapq.heappush(h, e)

while len(visited) < n:
    edge = heapq.heappop(h)

    if edge.x not in visited:
        visited.add(edge.x)
        out += edge.r

        for e in graph[edge.x]:
            heapq.heappush(h, e)
    elif edge.y not in visited:
        visited.add(edge.y)
        out += edge.r

        for e in graph[edge.y]:
            heapq.heappush(h, e)

print out
