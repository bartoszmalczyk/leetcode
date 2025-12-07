class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = [0]

        n = len(grid) #height
        m = len(grid[0]) #width

        walls_count = 0 
        start = (0,0)
        end = (0,0)

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    start = (r,c)
                elif grid[r][c] == 2:
                    end = (r,c)
                elif grid[r][c] == -1:
                    walls_count += 1
        
        required_steps = m * n - walls_count
        
        def backtracking(r,c,steps):
            if r >= n or r < 0 or c >= m or c < 0:
                return
            if grid[r][c] == -1:
                return
            if grid[r][c] == 2:
                if steps == required_steps:
                    ans[0] += 1
                return
            
            temp = grid[r][c]
            grid[r][c] = -1
            backtracking(r + 1, c, steps + 1)
            backtracking(r - 1, c, steps + 1)
            backtracking(r, c + 1, steps + 1)
            backtracking(r, c - 1, steps + 1)
            grid[r][c] = temp

        backtracking(start[0], start[1], 1)
        return ans[0]