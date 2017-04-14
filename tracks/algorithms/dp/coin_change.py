

n, m = [int(x) for x in raw_input().split()]
cs = [int(x) for x in raw_input().split()]

dp = [0] * (n + 1)
dp[0] = 1

import pdb; pdb.set_trace()
for i in range(1, n+1):
    for c in cs:
        if i - c >= 0:
            dp[i] += dp[i-c]

print dp[n]

