
from collections import deque


dc = [0, 1, 0, -1]
dr = [-1, 0, 1, 0]
ds = zip(dr, dc)

free_move = set(['.', '*'])


def explore(forest, n, m):
    start = None
    end = None

    for i in range(n):
        for j in range(m):
            if forest[i][j] == 'M':
                start = (i, j)
            if forest[i][j] == '*':
                end = (i, j)

    q = deque([start])

    forest[start[0]][start[1]] = 0

    while q:
        r, c = q.pop()

        if (r, c) == end:
            return forest[r][c]

        possible_moves = 0
        for ddr, ddc in ds:
            n_r = r + ddr
            n_c = c + ddc

            if n_r >= 0 and n_r < n and n_c >= 0 and n_c < m and forest[n_r][n_c] in free_move:
                possible_moves += 1

        for ddr, ddc in ds:
            n_r = r + ddr
            n_c = c + ddc

            if n_r >= 0 and n_r < n and n_c >= 0 and n_c < m and forest[n_r][n_c] in free_move:
                forest[n_r][n_c] = forest[r][c] + 1 if possible_moves > 1 else forest[r][c]
                q.appendleft((n_r, n_c))


t = int(raw_input())

for _ in range(t):
    n, m = [int(x) for x in raw_input().split()]

    forest = []
    for _ in range(n):
        forest.append(list(raw_input()))

    k = int(raw_input())

    turns = explore(forest, n, m)

    if turns == k:
        print "Impressed"
    else:
        print "Oops!"
