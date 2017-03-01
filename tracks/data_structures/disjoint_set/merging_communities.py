
class Node(object):
    def __init__(self, x):
        self.value = x
        self.parent = self
        self.rank = 0
        self.size = 1

class UnionFind(object):


    def __init__(self, n):
        self._nodes = [-1]

        for i in range(1, n+1):
            self._nodes.append(Node(i))


    def find(self, x):
        node = self._nodes[x]

        if node.parent == node:
            return node
        else:
            return self.find(node.parent.value)

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if x_root.rank < y_root.rank:
            x_root.parent = y_root
            y_root.size += x_root.size
        elif y_root.rank < x_root.rank:
            y_root.parent = x_root
            x_root.size += y_root.size
        else:
            y_root.parent = x_root
            x_root.rank += 1
            x_root.size += y_root.size


n, q = [int(x) for x in raw_input().split()]

uf = UnionFind(n)

for _ in range(q):
    l = raw_input().split()

    if l[0] == 'M':
        uf.union(int(l[1]), int(l[2]))
    else:
        node = uf.find(int(l[1]))
        print node.size
