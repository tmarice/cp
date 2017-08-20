
def main():
    x, a, b = (int(z) for z in input().split())

    if abs(a-x) < abs(b-x):
        print("A")
    else:
        print("B")


if __name__ == "__main__":
    main()
