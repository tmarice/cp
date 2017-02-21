
def cmp(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        for i in range(len(a)):
            if a[i] < b[i]:
                return -1
            elif a[i] > b[i]:
                return 1

        return 0


n = int(raw_input())
numbers = []

for _ in range(n):
    numbers.append(raw_input().strip())

numbers.sort(cmp)

for x in numbers:
    print x
