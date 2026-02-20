class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1: 
                    dp[r][c] = 0
                    continue
                else:
                    if r == 0 and c == 0:
                        if obstacleGrid[r][c] == 1: 
                            return 0
                        dp[r][c] = 1
                    elif r < 1:
                        dp[r][c] += dp[r][c - 1]
                    elif c < 1:
                        dp[r][c] += dp[r - 1][c]
                    else:
                        dp[r][c] += dp[r - 1][c]
                        dp[r][c] += dp[r][c - 1]
        return dp[m - 1][n - 1]