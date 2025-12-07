class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = [0]

        n = len(grid) #height
        m = len(grid[0]) #width

        start = (0,0)
        end = (0,0)

        ammount_walls = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == -1:
                    ammount_walls += 1
                elif grid[r][c] == 1:
                    start = (r,c)
                elif grid[r][c] == 2:
                    end = (r,c)
        required_steps = m*n - ammount_walls 

        def backtracking(r,c, steps):
            if r < 0 or r >= n or c < 0 or c >= m:
                return
            elif grid[r][c] == -1:
                return
            if grid[r][c] == 2:
                if steps == required_steps:
                    ans[0] += 1
                return
            else: 
                temp = grid[r][c]
                grid[r][c] = -1
                backtracking(r + 1,c, steps + 1)
                backtracking(r - 1,c, steps + 1)
                backtracking(r,c + 1, steps + 1)
                backtracking(r,c - 1, steps + 1)
                grid[r][c] = temp
        backtracking(start[0], start[1], 1)
        return ans[0]
            