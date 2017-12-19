
def main():
    step = int(input())

    res = 0
    pos = 0

    import pdb; pdb.set_trace()
    for i in range(1, 50000001):
        pos = (pos + step) % i

        if pos == 0:
            res = i

        pos += 1

    print(res)


if __name__ == "__main__":
    main()
