
import re

def getRegex(n, k):
    alphabet = ["<1", "<2", ">1", ">2", "+1", "+2", "-1", "-2"]
    states = []
    sm = {}
    transitions = set()

    i = 1
    for floor in range(1, n+1):
        for people in range(k+1):
            states.append((floor, people))

            sm[(floor, people)] = i
            i += 1

    for (floor, people) in states:
        #transitions.add(((floor, people), "EPS", (floor, people)))

        for diff in range(-2, 3):
            if diff == 0:
                continue

            # people variant
            new_people = people + diff

            if 0 <= new_people <= k:
                transitions.add((
                    (floor, people),
                    ">{0}".format(abs(diff)) if diff < 0 else "<{0}".format(diff),
                    (floor, new_people)
                ))

            # floor variant
            new_floor = floor + diff

            if 1 <= new_floor <= n:
                transitions.add((
                    (floor, people),
                    "+{0}".format(diff) if diff > 0 else "{0}".format(diff),
                    (new_floor, people)
                ))

    import pdb; pdb.set_trace()
    R = {}
    for s1 in states:
        for s2 in states:
            R[(sm[s1], sm[s2], 0)] = ""

            for sign in alphabet:
                if (s1, sign, s2) in transitions:
                    R[(sm[s1], sm[s2], 0)] = sign

    import pdb; pdb.set_trace()
    for k in range(1, len(states) + 1):
        for s1 in states:
            for s2 in states:
                R[(sm[s1], sm[s2], k)] = R[(sm[s1], sm[s2], k - 1)] + "|{0}({1})*{2}".format(
                        R[(sm[s1], k, k - 1)], R[(k, k, k -1)], R[(k, sm[s2], k - 1)])

    import pdb; pdb.set_trace()
    print(B[0])


n, k = list(map(int, input().split()))

r = getRegex(n, k)

m = int(input())
for _ in range(m):
    s = input()
    print("YES" if re.match(r, s) else "NO")
