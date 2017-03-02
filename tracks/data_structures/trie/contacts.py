import sys


class Node(object):

    def __init__(self, value=0):
        self.value = value
        self.sum = 0
        self.links = [None] * 26


    def get_link(self, c):
        return self.links[ord(c) - ord('a')]


    def add_link(self, c, node):
        self.links[ord(c) - ord('a')] = node


class Trie(object):

    def __init__(self):
        self.root = Node()


    def add(self, string):
        self.root = self._add(self.root, string, 0)


    def find_partial(self, string):
        node = self.root

        for c in string:
            if node is None:
                return 0

            node = node.get_link(c)

        if node is None:
            return 0
        else:
            return node.value + node.sum


    def _add(self, node, string, i):
        if i == len(string):
            return Node(1)
        if i > len(string):
            return None

        cur_node = node if node is not None else Node()

        new_node = self._add(cur_node.get_link(string[i]), string, i+1)

        cur_node.add_link(string[i], new_node)
        cur_node.sum = sum([x.sum for x in cur_node.links if x is not None] + [x.value for x in cur_node.links if x is not None])

        return cur_node


    def _count(self, node):
        if node is None:
            return 0
        else:
            return node.sum


n = int(raw_input())

trie = Trie()

sys.setrecursionlimit(1<<10)
for _ in range(n):
    op, word = raw_input().split()

    if op == "add":
        trie.add(word)
    elif op == "find":
        print trie.find_partial(word)
