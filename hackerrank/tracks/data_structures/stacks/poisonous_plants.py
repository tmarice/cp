"""
stack with (pesticide, days to die) values
add (p[0], 0) to stack

for every other plan:
    pop top of stack
    if current plant > top of stack, it will die on the first day, add to stack (plant, 1)
    else if current plant smaller than top of stack, keep popping off stack until stack empty or top of stack <= current plant
    keep track of largest number of days during popping
    if stack empty at end, add (plant, 0) to stack
    else add (plant, largest number of days + 1) to stack
"""

n = int(raw_input())
ps = [int(x) for x in raw_input().split()]

s = [] # (plant pesticide, days to die)
max_days = 0

for p in ps:
    days = 0

    while s and s[-1][0] >= p:
        plant, dtd = s.pop()
        days = max(days, dtd)

    dtd = days + 1 if s else 0
    s.append((p, dtd))
    max_days = max(max_days, dtd)

print max_days
