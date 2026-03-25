import numpy as np
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        sum_ = sum(grid[0])

        pre_rows = [sum(grid[0])]
        for i in range(1,m):
            temp = sum(grid[i])
            pre_rows.append(pre_rows[- 1] + temp)
            sum_ += temp
        pre_cols = []

        if sum_ % 2 != 0:
            return False

        for row in pre_rows:
            if row == sum_ - row: return True

        pre_col = [0]
        for i in range(m):
            pre_col[0] += grid[i][0]
        
        for i in range(1, n):
            temp = 0
            for j in range(m):
                temp += grid[j][i]
            pre_col.append(pre_col[-1] + temp)

        for col in pre_col:
            if col == sum_ - col: return True
        return False


