
q = int(raw_input())

history = []
s = ""

for _ in range(q):
    l = raw_input().split()

    if l[0] == '1':
        # append
        history.append(s)

        s += l[1]
    elif l[0] == '2':
        k = int(l[1])
        history.append(s)

        s = s[:-k]
    elif l[0] == '3':
        k = int(l[1])
        print s[k-1]

    elif l[0] == '4':
        s = history.pop()
