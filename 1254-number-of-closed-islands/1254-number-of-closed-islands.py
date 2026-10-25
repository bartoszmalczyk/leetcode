class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        seen = set()
        directions = {(1,0), (-1,0), (0, 1), (0, -1)}

        def dfs(i,j):
            if (i,j) in seen:
                return True
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return False
            if grid[i][j] == 1:
                return True
            seen.add((i,j))
            return dfs(i + 1,j) and dfs(i - 1, j) and dfs(i, j + 1) and dfs(i, j - 1)
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0 and (i,j) not in seen:
                    ans += dfs(i,j)        
        return ans
            
            

                