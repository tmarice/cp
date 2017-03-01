class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.links = {}


class Trie(object):

    def __init__(self):
        self.root = None


    def add(self, string):
        self._add(self.root, string, 0)


    def _add(self, node, string, i):
        if i >= len(string):
            return

        if node is not None:
                node.links[string[i]] = self._add(

        if node is None:
            n = Node()
            n.links[string[i]] = self._add(
