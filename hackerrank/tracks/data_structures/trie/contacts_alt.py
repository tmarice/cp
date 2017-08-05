from collections import defaultdict


class Trie(object):

    def __init__(self):
        self.trie = defaultdict(int)

    def add(self, string):
        for i in range(1, len(string)+1):
            self.trie[string[:i]] += 1

    def find(self, prefix):
        return self.trie[prefix]



n = int(raw_input())

trie = Trie()

for _ in range(n):
    op, word = raw_input().split()

    if op == "add":
        trie.add(word)
    elif op == "find":
        print trie.find(word)
