from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        ans = []
        seen = set()
        not_seen = set(range(1, n * n + 1)) 
        
        for arr in grid:
            for number in arr:
                if number in seen:
                    ans.append(number) 
                else:
                    seen.add(number)
                    not_seen.remove(number)  
        ans.append(not_seen.pop()) 
        return ans