

def megaprimes(start):
    digits = [2,3,5,7]

    n = len(start)

    x = [0] * n





first, last = raw_input().split()

count = 0
for p in megaprimes(first):
    count += 1
    if p > last:
        break

print count


