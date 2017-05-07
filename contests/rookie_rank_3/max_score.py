


class BitVector(object):

    def __init__(self, n=None, other=None):
        if n is not None:
            self._x = 2 ** n
            self._n = n
            self._unset = n
        elif other is not None:
            self._x = other._x
            self._n = other._n
            self._unset = other._unset


    def __len__(self):
        return self._unset


    @property
    def lowest_unset(self):
        # get index of lowest unset element
        mask = 1

        for i in range(self._n):
            if self._x & mask == 0:
                return i
            mask <<= 1


    def is_set(self, i):
        # is index i set?
        return self._x & (1 << i)


    def set(self, i):
        self._x = self._x | (1 << i)
        self._unset -= 1


    def __hash__(self):
        return hash(self._x)


memo = {}
xs = []
n = 0

def solve(state):
    if state in memo:
        return memo[state]

    if len(state) == 1:
        return 0, xs[state.lowest_unset] # score_i, running_sum

    score = 0
    running_sum = 0
    for i in range(n):
        if not state.is_set(i):
            new_state = BitVector(other=state)
            new_state.set(i)

            cur_score, cur_running_sum = solve(new_state)

            if cur_score + cur_running_sum % xs[i] > score:
                score = cur_score + cur_running_sum % xs[i]
                running_sum = cur_running_sum + xs[i]

    r = (score, running_sum)
    memo[state] = r

    return r


def main():
    global n, xs
    n = int(raw_input())
    xs = [int(x) for x in raw_input().split()]

    
    print solve(BitVector(n))[0]


if __name__ == "__main__":
    main()
