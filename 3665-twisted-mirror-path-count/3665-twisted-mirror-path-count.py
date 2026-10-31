class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j][0] = 1
                    dp[i][j][1] = 1
                    continue
    
                from_top = dp[i - 1][j][1] if i - 1 >= 0 else 0
                from_left = dp[i][j - 1][0] if j - 1 >= 0 else 0
                
                if grid[i][j] == 0:
                    total = (from_top + from_left) % MOD
                    dp[i][j][0] = total
                    dp[i][j][1] = total
                else:
                    dp[i][j][0] = from_top
                    dp[i][j][1] = from_left
                    
        return dp[m - 1][n - 1][0]