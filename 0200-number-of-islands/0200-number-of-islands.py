class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = {(0,1), (0,-1), (1,0), (-1,0)}
        m = len(grid)
        n = len(grid[0])
        counter = 0
        def is_valid(r,c):
            return True if (
                r >= 0 and r < m and
                c >= 0 and c < n
                ) else False

        def dfs(r,c):
            if not is_valid(r,c) or grid[r][c] == "0" or (r,c) in visited:
                return
            visited.add((r,c))
            for rr,cc in directions:
                dfs(r + rr,c + cc)

        for r in range(m):
            for c in range(n):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    counter += 1
        return counter
                
            
