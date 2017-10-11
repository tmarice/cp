


def main():
    rows, cols = (int(x) for x in input().split())
    mat = []

    for _ in range(rows):
        mat.append(input().split())

    for i in range(cols):
        for j in range(rows):
            print(mat[j][i], end=" ")
        print()

main()




