def has_cycle(head):
    if head is None:
        return False

    single = head
    try:
        double = head.next.next
    except:
        return False

    while single is not double:
        single = single.next
        try:
            double = double.next.next
        except:
            return False

        if single is None or double is None:
            return False

    return True


