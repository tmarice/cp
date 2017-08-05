
from collections import deque

MOD = 10 ** 9
cache = {}

def get_paths(r_graph, node):
    if node in cache:
        return cache[node]
    
    if node == 0:
        return 1

    ret = 0

    for c in r_graph[node]:
        ret += get_paths(r_graph, c)
        ret %= MOD

    cache[node] = ret

    return ret


visited = set()
stack = set()

def has_cycle(graph, node):
    if node not in visited:
        visited.add(node)
        stack.add(node)

        for c in graph[node]:
            if c not in visited and has_cycle(graph, c) :
                return True
            if c in stack:
                return True


    stack.remove(node)
    return False


n, m = [int(x) for x in raw_input().split()]

r_graph = {x: set() for x in xrange(n)}

for _ in xrange(m):
    x, y = [int(x) for x in raw_input().split()]
    x -= 1
    y -= 1

    r_graph[y].add(x)

if has_cycle(r_graph, n-1):
    print "INFINITE PATHS"
else:
    print get_paths(r_graph, n-1)
