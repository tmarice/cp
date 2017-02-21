# def FindMergeNode(headA, headB):
#     while headA:
#         next = headA.next
#         headA.next = None
#         headA = next

#     while True:
#         if headB.next is None:
#             return headB.data

#         headB = headB.next


def get_len(head):
    l = 0

    while head:
        l += 1
        head = head.next

    return l


def advance(head, x):
    for _ in xrange(x):
        head = head.next

    return head


def FindMergeNode(headA, headB):
    lenA = get_len(headA)
    lenB = get_len(headB)

    if lenA > lenB:
        headA = advance(headA, lenA-lenB)
    else:
        headB = advance(headB, lenB-lenA)

    while headA is not headB:
        headA = headA.next
        headB = headB.next

    return headA.data
