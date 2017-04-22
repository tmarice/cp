
import heapq

n = int(raw_input())
h = []

for i in range(n):
    line = raw_input()
    if line[0] == 's': #store next email
        _, content, urgency = line.split()
        urgency = int(urgency)
        heapq.heappush(h, (-urgency, i, content))
    else: # get next email
        try:
            _, _, content = heapq.heappop(h)
        except IndexError:
            content = '-1'

        print content
