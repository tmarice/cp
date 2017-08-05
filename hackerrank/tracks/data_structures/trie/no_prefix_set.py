
n = int(raw_input())

string_trie = set()
prefix_trie = set()

found = None

for _ in range(n):
    s = raw_input()

    if found is None:
        if s in prefix_trie:
            found = s

        for i in range(1, len(s)+1):
            if s[:i] in string_trie:
                found = s
                break
            prefix_trie.add(s[:i])

        string_trie.add(s)


if found:
    print "BAD SET"
    print found
else:
    print "GOOD SET"
