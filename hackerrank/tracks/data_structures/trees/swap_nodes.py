import sys

class Node(object):
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def inorder(self):
        if self.left:
            self.left.inorder()

        print self.value,

        if self.right:
            self.right.inorder()


def swap(root, k, d):
    if root is None:
        return

    if d % k == 0:
        root.left, root.right = root.right, root.left

    swap(root.left, k, d+1)
    swap(root.right, k, d+1)


def main():
    n = int(raw_input())
    nodes = {x: Node(x) for x in range(1, n+1)}

    for i in range(1, n+1):
        l,r = [int(x) for x in raw_input().split()]

        if l != -1:
            nodes[i].left = nodes[l]

        if r != -1:
            nodes[i].right = nodes[r]

    root = nodes[1]

    t = int(raw_input())

    while t:
        k = int(raw_input())
        swap(root, k, 1)

        root.inorder()
        print

        t -= 1


if __name__ == "__main__":
    sys.setrecursionlimit(1<<20)
    main()

