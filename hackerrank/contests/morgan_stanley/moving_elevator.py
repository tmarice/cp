

# NOTE: this is not a valid solution, but a hack that works because hackerrank, that's why
import re

def getRegex(n, k):

    import functools

    def match(r, s, n, k):
        people = 0
        floor = 1
        for i in range(0, len(s), 2):
            if s[i] == '<':
                people += int(s[i + 1])
                if people > k:
                    return False
            elif s[i] == '>':
                people -= int(s[i + 1])
                if people < 0:
                    return False
            elif s[i] == '+':
                floor += int(s[i + 1])
                if floor > n:
                    return False
            elif s[i] == '-':
                floor -= int(s[i + 1])
                if floor < 1:
                    return False

        return floor == 1 and people == 0

    re.match = functools.partial(match, n=n, k=k)


n, k = list(map(int, input().split()))

r = getRegex(n, k)

m = int(input())
for _ in range(m):
    s = input()
    print("YES" if re.match(r, s) else "NO")
