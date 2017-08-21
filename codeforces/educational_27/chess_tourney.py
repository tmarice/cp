
def main():
    n = int(input())
    rs = sorted([int(x) for x in input().split()], reverse=True)

    if rs[n-1] > rs[n]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
