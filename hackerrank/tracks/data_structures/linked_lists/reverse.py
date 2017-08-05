

def Reverse(head):
    if head is None:
        return head

    n = head.next
    head.next = None

    while n:
        t = n.next
        n.next = head
        head = n
        n = t

    return head
