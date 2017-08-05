class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def append(self, x):
        self.s1.append(x)

    def front(self):
        if len(self.s2) == 0:
            self._restack()
        
        return self.s2[-1]

    def pop(self):
        if len(self.s2) == 0:
            self._restack()

        return self.s2.pop()

    def _restack(self):
        while self.s1:
            self.s2.append(self.s1.pop())


q = int(raw_input())

queue = Queue()

for _ in range(q):
    l = raw_input().split()
    if l[0] == '1':
        queue.append(l[1])
    elif l[0] == '2':
        queue.pop()
    else:
        print queue.front()
