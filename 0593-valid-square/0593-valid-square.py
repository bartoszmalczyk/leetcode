from typing import List
from itertools import combinations
import math

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        arr = [p1,p2,p3,p4]
        comb = combinations(arr, 2)
        length = []
        for a,b in comb:
            length.append(math.dist(a, b))
        length.sort()
        if length[0] <= 0:
            return False
        print(length)
        if length[0] == length[1] and length[1] == length[2] and length[2] == length[3] and length[4] == length[5]:
            if round(math.sqrt(pow(length[0],2) + pow(length[1],2)),7) == round(length[4],7):
                return True
        else:
            return False
        
sol = Solution()
print(sol.validSquare([0,0], [1,1], [1,0], [0,1]))