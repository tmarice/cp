

n = int(raw_input())
k = int(raw_input())
xs = [int(raw_input()) for _ in range(n)]

xs.sort()

minimum = 0
maximum = k - 1
unfairness = xs[maximum] - xs[minimum]

while maximum < n:
    unfairness = min(unfairness, xs[maximum] - xs[minimum])

    maximum += 1
    minimum += 1

print unfairness
