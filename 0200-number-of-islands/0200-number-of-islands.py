class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = {(0,1), (0,-1), (1,0), (-1,0)}
        m = len(grid)
        n = len(grid[0])
        counter = 0
        def is_valid(r,c):
            return 0 <= r < m and 0 <= c < n

        def dfs(r,c):
            if not is_valid(r,c) or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for rr,cc in directions:
                dfs(r + rr,c + cc)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r,c)
                    counter += 1
        return counter
                
            
