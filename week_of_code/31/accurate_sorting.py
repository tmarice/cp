
def check_sorted(a, n):
    for i in range(n-1):
        if a[i] > a[i+1]:
            return "No"

    return "Yes"


def swap(a, n):
    for i in range(n-1):
        if a[i] > a[i+1] and a[i] - a[i+1] == 1:
            a[i], a[i+1] = a[i+1], a[i]


def main():
    q = int(raw_input())

    for _ in range(q):
        n = int(raw_input())
        a = [int(x) for x in raw_input().split()]

        swap(a, n)
        print check_sorted(a, n)


if __name__ == "__main__":
    main()
