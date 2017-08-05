class Stacks:

    def __init__(self, s1, s2, s3):
        self._stacks = [s1, s2, s3]
        self._sums = [sum(s1), sum(s2), sum(s3)]


    @property
    def equal(self):
        return self._sums[0] == self._sums[1] and self._sums[1] == self._sums[2]


    def pop(self, i):
        x = self._stacks[i].pop()
        self._sums[i] -= x


    def height(self, i):
        return self._sums[i]


    def find_max(self):
        s = sorted(zip(self._sums, xrange(3)), reverse=True)

        if s[0][0] == s[1][0]:
            if self._stacks[s[0][1]][-1] < self._stacks[s[1][1]][1]:
                return s[0][1]
            else:
                return s[1][1]

        return s[0][1]


n1, n2, n3 = [int(x) for x in raw_input().split()]

s1 = [int(x) for x in raw_input().split()]
s2 = [int(x) for x in raw_input().split()]
s3 = [int(x) for x in raw_input().split()]

s1.reverse()
s2.reverse()
s3.reverse()

stacks = Stacks(s1, s2, s3)

while not stacks.equal:
    i = stacks.find_max()
    stacks.pop(i)

print stacks.height(0)
