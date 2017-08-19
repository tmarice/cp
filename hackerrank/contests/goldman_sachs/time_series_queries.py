
import bisect

INF = 10 ** 9 + 1


class DataChurner(object):

    def __init__(self, n, ts, ps):
        self._n = n

        self._ts_by_ps = []
        self._ps_by_ps = []

        self._min_ts_by_pos = []

        for p, t in sorted(zip(ps, ts)):
            self._ts_by_ps.append(t)
            self._ps_by_ps.append(p)

        cur_min = INF
        for t in reversed(self._ts_by_ps):
            if t < cur_min:
                cur_min = t

            self._min_ts_by_pos.append(cur_min)

        self._min_ts_by_pos = list(reversed(self._min_ts_by_pos))

################################################################################

        self._ts_by_ts = []
        self._ps_by_ts = []

        self._max_ps_by_pos = []

        for t, p in sorted(zip(ts, ps)):
            self._ts_by_ts.append(t)
            self._ps_by_ts.append(p)

        cur_max = -1
        for p in reversed(self._ps_by_ts):
            if p > cur_max:
                cur_max = p

            self._max_ps_by_pos.append(cur_max)

        self._max_ps_by_pos = list(reversed(self._max_ps_by_pos))


    def get_earliest_timestamp(self, price):
        #import pdb; pdb.set_trace()
        pos = bisect.bisect_left(self._ps_by_ps, price)

        if pos >= self._n:
            return -1
        else:
            return self._min_ts_by_pos[pos]


    def get_maximum_value(self, ts):
        #import pdb; pdb.set_trace()
        pos = bisect.bisect_left(self._ts_by_ts, ts)

        if pos >= self._n:
            return -1
        else:
            return self._max_ps_by_pos[pos]


def main():
    xs = []
    try:
        while True:
            xs.extend([int(x) for x in input().split()])
    except:
        pass

    n, q = xs[0], xs[1]
    ts = xs[2:2+n]
    ps = xs[2+n:2*2*n]

#    n, q = (int(x) for x in input().split())
#    ts = [int(x) for x in input().split()]
#    ps = [int(x) for x in input().split()]

    dc = DataChurner(n, ts, ps)

    for i in range(q):
        t, v = xs[2+2*n+2*i], xs[2+2*n+2*i+1]
#        t, v = (int(x) for x in input().split())
        
        if t == 1:
            print(dc.get_earliest_timestamp(v))
        else:
            print(dc.get_maximum_value(v))


if __name__ == "__main__":
    main()


