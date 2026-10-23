class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        seen = set()
        perimeter = 0
        directions = {(1,0), (-1,0), (0,1), (0,-1)}
        def dfs(i,j):
            nonlocal perimeter 
            if (i,j) in seen or i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            for x,y in directions:
                if i + x < 0 or i + x >= m or j + y < 0 or j + y >= n:
                    perimeter += 1
                elif grid[i + x][j + y] == 0:
                    perimeter += 1
            seen.add((i,j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return perimeter
        
