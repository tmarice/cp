
def SortedInsert(head, data):
    # list is empty
    if head is None:
        return Node(data)

    if  head.next is None or head.data <= data <= head.next.data:
        node = Node(data, next_node=head.next, prev_node=head)
        head.next = node
        return head

    head.next = SortedInsert(head.next, data)
    return head
