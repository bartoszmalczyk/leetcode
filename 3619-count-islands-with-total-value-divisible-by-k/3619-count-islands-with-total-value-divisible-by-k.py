class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        ans = 0
        curr = 0
        def dfs(i,j):
            nonlocal curr
            if (i,j) in seen:
                return 
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return 
            if grid[i][j] == 0:
                return 
            seen.add((i,j))
            curr += grid[i][j]
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i,j) not in seen:
                    curr = 0 
                    dfs(i,j)
                    if curr % k == 0:
                        ans += 1
                    seen.add((i,j))
        return ans