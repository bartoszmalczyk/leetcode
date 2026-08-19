from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        hm = defaultdict(set)
        
        for r, c in reservedSeats:
            hm[r].add(c) 
            
        counter = (n - len(hm)) * 2

        for row in hm:
            left = not {2, 3, 4, 5}.intersection(hm[row])
            middle = not {4, 5, 6, 7}.intersection(hm[row])
            right = not {6, 7, 8, 9}.intersection(hm[row])
            
            if left and right:
                counter += 2
            elif left or right or middle:
                counter += 1
                    
        return counter