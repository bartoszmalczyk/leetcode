class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r - 1 < 0 and c - 1 < 0:
                    dp[r][c].add(grid[0][0])
                    continue 
                if c - 1 >= 0:
                    for j in dp[r][c - 1]:
                        dp[r][c].add(grid[r][c] ^ j)
                if r - 1 >= 0:
                    for i in dp[r - 1][c]:
                        dp[r][c].add(grid[r][c] ^ i)

        ans = float('inf')
        for candidate in dp[-1][-1]:
            print(candidate)
            if candidate < ans:
                ans = candidate
        return ans