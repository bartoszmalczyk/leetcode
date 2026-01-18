from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def isMagic(r, c, size): 
            ref = sum(grid[r][c : c + size])
            for i in range(size):
                if sum(grid[r + i][c : c + size]) != ref: 
                    return False
            for j in range(size):
                col_sum = 0
                for i in range(size):
                    col_sum += grid[r + i][c + j]
                if col_sum != ref:
                    return False
            diag1 = diag2 = 0
            for k in range(size):
                diag1 += grid[r + k][c + k]
                diag2 += grid[r + k][c + size - 1 - k]
            if diag1 != ref or diag2 != ref:
                return False
            return True
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if isMagic(r, c, k):
                        return k
        return 1