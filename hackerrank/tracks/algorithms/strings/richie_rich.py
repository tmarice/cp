
import sys

n, k = [int(x) for x in raw_input().split()]
s = [int(x) for x in raw_input()]

modified = [False for _ in range(n)]

for i in range(n/2):
    d1 = s[i]
    d2 = s[n-i-1]

    if d1 > d2:
        s[n-i-1] = d1
        modified[i] = True
        k -= 1
    elif d2 > d1:
        s[i] = d2
        modified[i] = True
        k -= 1

for i in range(n/2):
    if k <= 0:
        break

    if modified[i] and k > 0 and s[i] != 9:
        s[n-i-1] = 9
        s[i] = 9
        k -= 1
    elif not modified[i] and k > 1 and s[i] != 9:
        s[n-i-1] = 9
        s[i] = 9
        k -= 2

if n % 2 != 0 and k > 0:
    s[n/2] = 9

if k < 0:
    print -1
else:
    print ''.join([str(x) for x in s])
