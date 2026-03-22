import numpy as np
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        mat = np.array(mat)
        target = np.array(target)

        for _ in range(3):
            mat = np.rot90(mat)
            if np.array_equal(mat,target):
                return True
        return False