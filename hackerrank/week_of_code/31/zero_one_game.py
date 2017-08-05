

g = int(raw_input())

for _ in range(g):
    n = int(raw_input())
    cs = raw_input().split()

    parts = []
    start = 0
    cur = 0
    while cur < len(cs)-1:
        if cs[cur] == '1' and cs[cur+1] == '1':
            sp = cs[start:cur]
            if sp:
                parts.append(sp)

            while cur < len(cs) and cs[cur] == '1':
                cur += 1

            start = cur

        cur += 1

    sp = cs[start:cur+1]
    if sp:
        parts.append(sp)

    output = 0
    for part in parts:
        i = 0
        while i < len(part) and part[i] == '1':
            i += 1
        if i < len(part):
            i += 1

        j = len(part)-1
        while j >= 0 and part[j] == '1':
            j -= 1
        if j >= 0:
            j -= 1

        if i <= j:
            output ^= (j - i + 1) % 2

    if output == 0:
        print "Bob"
    else:
        print "Alice"








