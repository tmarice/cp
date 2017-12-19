

class Node():
    __slots__ = ["x", "next"]

    def __init__(self, x, next_node=None):
        if next_node is None:
            self.next = self
        else:
            self.next = next_node

        self.x = x


def main():
    step = int(input())

    ll = Node(0)

    for i in range(1, 2018):
        for _ in range(step):
            ll = ll.next

        ll.next = Node(i, ll.next)
        ll = ll.next

    print(ll.next.x)


if __name__ == "__main__":
    main()
