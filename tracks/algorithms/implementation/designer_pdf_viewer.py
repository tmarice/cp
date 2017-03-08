
hs = [int(x) for x in raw_input().split()]
s = raw_input()

out = 0
for c in s:
    h = hs[ord(c) - ord('a')]
    out = max(out, h)

print out * len(s)
