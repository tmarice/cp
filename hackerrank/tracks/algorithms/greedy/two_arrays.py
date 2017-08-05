
q = int(raw_input())

for _ in range(q):
    n, k = [int(x) for x in raw_input().split()]
    a = [int(x) for x in raw_input().split()]
    b = [int(x) for x in raw_input().split()]

    for x, y in zip(sorted(a), sorted(b, reverse=True)):
        if x + y < k:
            print "NO"
            break
    else:
        print "YES"


