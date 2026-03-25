import numpy as np
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        grid = np.array(grid) 
        
        for i in range(0, m):
            if np.sum(grid[:i, :]) == np.sum(grid[i:, :]):
                return True
        for j in range(0, n):
            if np.sum(grid[:, :j]) == np.sum(grid[:, j:]):
                return True
        return False