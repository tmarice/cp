

def main():
    q = int(input())

    for _ in range(q):
        n, k, x, d = (int(z) for z in input().split())
        ts = (int(z) for z in input().split())

        fee = sum(max(k, t/100 * x) for t in ts)

        if fee > d:
            print("upfront")
        else:
            print("fee")


if __name__ == "__main__":
    main()
