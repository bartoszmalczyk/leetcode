class Solution:
    def numOfWays(self, n: int) -> int:
        #dp = [ai, bi], ai - ABA, bi ABC
        first = [6,6]
        second = [30, 24]

        if n == 1: return 12

        for _ in range(n - 2):
            first, second = second, [second[0] * 3 + second[1] * 2, second[0] * 2 + second[1] * 2]
        return sum(second) % (10**9 + 7)