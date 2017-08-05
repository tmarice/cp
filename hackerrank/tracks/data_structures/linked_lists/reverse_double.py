
def Reverse(head):
    if head is None:
        return head

    p = head.prev
    n = head.next

    while head:
        head.next = p
        head.prev = n

        if n is not None:
            head = n
            p = head.prev
            n = head.next
        else:
            return head


# 6     4       2
# n,4   6,2     4,n
# 4,n   2,6     n,4 
