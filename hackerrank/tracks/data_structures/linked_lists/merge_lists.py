
def MergeLists(headA, headB):
    if headA is None:
        return headB

    if headB is None:
        return headA

    if headA.data < headB.data:
        head = headA
        headA = headA.next
    else:
        head = headB
        headB = headB.next

    cur = head

    while headA is not None and headB is not None:
        if headA.data < headB.data:
            cur.next = headA
            headA = headA.next
        else:
            cur.next = headB
            headB = headB.next

        cur = cur.next

    if headA is None:
        cur.next = headB
    else:
        cur.next = headA

    return head



