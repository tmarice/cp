
def main():
    state = [int(x) for x in input().split()]
    n = len(state)

    history = set()
    steps = 0

    state_im = tuple(state)
    while state_im not in history:
        history.add(state_im)

        blocks, index = max((b, -i) for i, b in enumerate(state))
        index = -index

        state[index] = 0
        while blocks:
            index = (index + 1) % n
            state[index] += 1
            blocks -= 1

        steps += 1
        state_im = tuple(state)

    print(steps)


if __name__ == "__main__":
    main()
