"""
if stack is empty or top of stack smaller than current histogram:
    push to stack
else if current histogram smaller than top of stack:
    - effectively try all blocks that can be made up to top of stack histogram
    - declare top of stack to be the minimum
    - left border = index of previous element on stack - it has to be smaller that top of stack
    - right border = current index
    - area = (right - left) * top of stack
    do this while top of stack greater than current element

at the end, empty stack
"""
    

n = int(raw_input())
hs = [int(x) for x in raw_input().split()]

s = []
max_area = 0

for i, h in enumerate(hs):
    if s == [] or h >= s[-1][0]:
        s.append((h, i))
    else:
        while s and s[-1][0] > h:
            cur_h, cur_i = s.pop()
            k = i - (s[-1][1] + 1 if s else 0)

            max_area = max(max_area, k * cur_h)

        s.append((h, i))

if s:
    i = s[-1][1] + 1

    while s:
        cur_h, cur_i = s.pop()
        k = i - (s[-1][1] + 1 if s else 0)

        max_area = max(max_area, k * cur_h)

print max_area
            

