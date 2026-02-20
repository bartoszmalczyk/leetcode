class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
            
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1: 
                    dp[r][c] = 0
                elif r == 0 and c == 0:
                    dp[r][c] = 1
                elif r == 0:  
                    dp[r][c] = dp[r][c - 1]
                elif c == 0:  
                    dp[r][c] = dp[r - 1][c]
                else:        
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
                    
        return dp[m - 1][n - 1]