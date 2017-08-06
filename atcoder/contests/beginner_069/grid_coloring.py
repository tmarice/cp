


def main():
    h, w = (int(x) for x in input().split())
    n = int(input())
    ax = [int(x) for x in input().split()]

    cur_color = 0
    output = [[0] * w for _ in range(h)]

    for i in range(h):
        if i % 2 == 0:
            items = range(0, w)
        else:
            items = range(w-1, -1, -1)

        for j in items:
            output[i][j] = cur_color + 1

            ax[cur_color] -= 1
            if ax[cur_color] == 0:
                cur_color += 1
    
    for i in range(h):
        for j in range(w):
            print(output[i][j], end=" ")
        print()


if __name__ == "__main__":
    main()





