

from collections import deque


def main():
    n = int(raw_input())
    xs = (int(x) for x in raw_input().split())

    side = 0
    q = deque()

    for x in xs:
        if side == 0:
            q.append(x)
        else:
            q.appendleft(x)

        side = not side

    while q:
        if side == 0:
            print q.popleft(),
        else:
            print q.pop(),


if __name__ == "__main__":
    main()




    


