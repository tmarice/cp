def castleTowers(n, ar):
    max_n = ar[0]
    count = 0
    for a in ar:
        if a == max_n:
            count += 1
        elif a > max_n:
            max_n = a
            count = 1
            
    return count

