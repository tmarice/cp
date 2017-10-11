

from collections import defaultdict
from collections import deque
import heapq


def solve(services, tellers, q):
    queues = {i: deque() for i in tellers.keys()}

    target = len(q) - 1

    for i, item in enumerate(q):
        for k, v in queues.items():
            if item in tellers[k]:
                v.appendleft((i, item))

    q_times = [(0, i) for i in tellers.keys()]
    served = set()

    while True:
        cur_time, cur_q = heapq.heappop(q_times)

        cur_idx, cur_type = queues[cur_q].pop()

        if cur_idx == target:
            return cur_time

        while cur_idx in served:
            cur_idx, cur_type = queues[cur_q].pop()

        served.add(cur_idx)
        heapq.heappush(q_times, (cur_time + services[cur_type], cur_q))



def main():
    services = {}
    tellers = defaultdict(set)

    for l in input().strip().split(";"):
        l = l[1:-1]
        s, dur = l.split(",")
        dur = int(dur)
        services[s] = dur

    for l in input().strip().split(";"):
        l = l[1:-1]
        t, ss = l.split(",", 1)
        ss = ss[1:-1]
        tellers[int(t)] = set(ss.split(","))

    q = input().strip().split(",")

    me = input().strip()
    q.append(me)

    print(solve(services, tellers, q))


main()





