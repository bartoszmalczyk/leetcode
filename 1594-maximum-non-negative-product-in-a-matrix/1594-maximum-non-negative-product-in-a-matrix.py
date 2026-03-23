class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])
        dp = []
        for i in range(m):
            dp.append([])
            for j in range(n): 
                dp[i].append([-1, 1])
        dp[0][0] = (grid[0][0], grid[0][0])

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j][0] = min(dp[i][j - 1][0] * val, dp[i][j - 1][1] * val)
                    dp[i][j][1] = max(dp[i][j - 1][0] * val, dp[i][j - 1][1] * val)
                elif j == 0:
                    dp[i][j][0] = min(dp[i - 1][j][0] * val, dp[i - 1][j][1] * val)
                    dp[i][j][1] = max(dp[i - 1][j][0] * val, dp[i - 1][j][1] * val)
                else:
                    dp[i][j][0] = min(dp[i - 1][j][0] * val, dp[i - 1][j][1] * val, dp[i][j - 1][0] * val, dp[i][j - 1][1] * val)
                    dp[i][j][1] = max(dp[i][j - 1][0] * val, dp[i][j - 1][1] * val, dp[i - 1][j][0] * val, dp[i - 1][j][1] * val)
                    
        ans = dp[m - 1][n - 1][1]
        if ans < 0: return -1
        else: return ans % MOD

