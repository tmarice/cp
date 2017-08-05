
open_brackets = set(['(', '[', '{'])

brackets = {
    ')': '(',
    '}': '{',
    ']': '[',
}

def is_balanced(line):
    s = []

    for c in line:
        if c in open_brackets:
            s.append(c)
        else:
            if s and s[-1] == brackets[c]:
                s.pop()
            else:
                return False

    if s:
        return False
    else:
        return True
            

n = int(raw_input())

for _ in range(n):
    line = raw_input()

    if is_balanced(line):
        print 'YES'
    else:
        print 'NO'

