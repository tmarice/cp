
class MinHeap:

    def __init__(self, data=None):
        self._items = [-1]
        self._indices = {}

        if data is not None:
            #heapify data
            pass


    def push(self, x):
        self._items.append(x)
        i = len(self._items) - 1

        self._indices[x] = i
        self._float(i)


    def pop(self, x):
        i = self._indices[x]

        self._indices[self._items[-1]] = i
        self._items[i] = self._items[-1]

        self._items.pop()
        del self._indices[x]

        if len(self._items) > 1:
            self._sink(i)


    def min(self):
        return self._items[1]

    
    def _sink(self, i):
        if 2*i < len(self._items) and self._items[i] > self._items[2*i]:
            self._indices[self._items[i]], self._indices[self._items[2*i]] = self._indices[self._items[2*i]], self._indices[self._items[i]]
            self._items[i], self._items[2*i] = self._items[2*i], self._items[i]
            self._sink(2*i)

        if 2*i + 1 < len(self._items) and self._items[i] > self._items[2*i+1]:
            self._indices[self._items[i]], self._indices[self._items[2*i+1]] = self._indices[self._items[2*i+1]], self._indices[self._items[i]]
            self._items[i], self._items[2*i+1] = self._items[2*i+1], self._items[i]
            self._sink(2*i+1)


    def _float(self, i):
        if i > 1 and self._items[i] < self._items[i/2]:
            self._indices[self._items[i]], self._indices[self._items[i/2]] = self._indices[self._items[i/2]], self._indices[self._items[i]]
            self._items[i], self._items[i/2] = self._items[i/2], self._items[i]
            self._float(i/2)



q = int(raw_input())
heap = MinHeap()

for _ in range(q):
    l = raw_input().split()

    if l[0] == '1':
        heap.push(int(l[1]))
    elif l[0] == '2':
        heap.pop(int(l[1]))
    elif l[0] == '3':
        print heap.min()




