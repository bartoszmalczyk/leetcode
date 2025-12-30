class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(r, c):
            #check if unique and < 10
            seen = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    val = grid[i][j]
                    if val < 1 or val > 9 or val in seen:
                        return False
                    seen.add(val)
            
            #rows sum check
            for i in range(r, r + 3):
                if sum(grid[i][c:c+3]) != 15:
                    return False
            
            # cols sum check
            for j in range(c, c + 3):
                if grid[r][j] + grid[r+1][j] + grid[r+2][j] != 15:
                    return False
            
            # diagonals
            diag1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
            diag2 = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]
            
            if diag1 != 15 or diag2 != 15:
                return False
            return True

        rows, cols = len(grid), len(grid[0])
        ans = 0
        for i in range(rows - 2):
            for j in range(cols - 2):  
                if isMagic(i, j):
                    ans += 1
        return ans