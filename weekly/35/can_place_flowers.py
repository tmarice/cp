
class Solution(object):

    def canPlaceFlowers(self, flowerbed, n):
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n <= 1
            else:
                return n == 0

        for i, x in enumerate(flowerbed):
            if x == 0:
                if i == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1

        return n <= 0


def main():
    s = Solution()
    t = [int(x) for x in raw_input().split()]
    n = int(raw_input())

    print s.canPlaceFlowers(t, n)

main()
    


