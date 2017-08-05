

def find_point(cumsum):
    if len(cumsum) == 1:
        return "YES"

    for i in range(len(cumsum)-1):
        if cumsum[i] == cumsum[-1] - cumsum[i+1]:
            return "YES"

    if cumsum[-1] == 0:
        return "YES"

    return "NO"


t = int(raw_input())

for _ in range(t):
    n = int(raw_input())
    a = [int(x) for x in raw_input().split()]

    cumsum = [a[0]]

    for x in a[1:]:
        cumsum.append(x+cumsum[-1])

    print find_point(cumsum)
