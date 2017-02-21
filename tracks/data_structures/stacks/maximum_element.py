

class Stack:

    def __init__(self):
        self._l = []
        self._max = []


    def pop(self):
        r = self._l.pop()
        if self._max[-1] == r:
            self._max.pop()

        return r


    def push(self, x):
        self._l.append(x)

        if len(self._max) == 0 or x >= self._max[-1]:
            self._max.append(x)


    @property
    def max(self):
        return self._max[-1]


def main():
    n = int(raw_input())

    s = Stack()

    for _ in range(n):
        l = [int(x) for x in raw_input().split()]

        if l[0] == 1:
            s.push(l[1])
        elif l[0] == 2:
            s.pop()
        else:
            print s.max


if __name__ == "__main__":
    main()
