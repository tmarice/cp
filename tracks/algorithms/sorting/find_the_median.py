

def partition(a, left, right):
    pivot_index = left
    pivot_value = a[left]
    a[pivot_index], a[right] = a[right], a[pivot_index]

    for i in range(left, right):
        if a[i] < pivot_value:
            a[i], a[pivot_index] = a[pivot_index], a[i]
            pivot_index += 1

    a[pivot_index], a[right] = a[right], a[pivot_index]

    return pivot_index


def quickselect(a, left, right, k):
    pivot = partition(a, left, right)

    if pivot == k:
        return a[k]
    elif k < pivot:
        return quickselect(a, left, pivot-1, k)
    else:
        return quickselect(a, pivot+1, right, k)



n = int(raw_input())
a = [int(x) for x in raw_input().split()]

if n % 2:
    print quickselect(a, 0, len(a)-1, n/2)
else:
    print (quickselect(a, 0, len(a)-1, n/2) + quickselect(a, 0, len(a)-1, n/2+1)) / 2

