
from collections import defaultdict



trans = defaultdict(list)
s = ""
pool = {}
memo = {}


def ff(n):
    t = 0
    visited = set()

    for i in range(1, n+1):
        if i not in visited:
            st = [i]
            visited.add(i)
            while st:
                c = st.pop()
                pool[c] = t

                for neigh in trans[c]:
                    if neigh not in visited:
                        visited.add(neigh)
                        st.append(neigh)

            t += 1



def can_equate(a, b):
    return pool[a] == pool[b]



def transform(first, last):
    if first >= last:
        return 0
    elif (first, last) in memo:
        return memo[(first, last)]
    else:
        if first == last or can_equate(s[first], s[last]):
            r = transform(first + 1, last - 1)
        else:
            r = 1 + min(transform(first + 1, last), transform(first, last - 1))

        memo[(first, last)] = r
        return r



def main():
    global s

    n, k, m = [int(x) for x in raw_input().split()]

    for _ in range(k):
        a, b = [int(x) for x in raw_input().split()]
        trans[b].append(a)
        trans[a].append(b)

    ff(n)

    s = [int(x) for x in raw_input().split()]

    print len(s) - transform(0, m - 1)


main()
