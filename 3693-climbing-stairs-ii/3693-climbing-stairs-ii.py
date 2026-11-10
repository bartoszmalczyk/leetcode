class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 3)
        for i in range(3, n + 3):
            dp[i] = min(dp[i - 1] + costs[i - 3] + 1, dp[i - 2]+ costs[i - 3] + 4, dp[i - 3]+ costs[i - 3] + 9)

        return dp[-1]
