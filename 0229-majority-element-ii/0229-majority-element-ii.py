from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2 = 0, 0
        f, s = None, None
        for num in nums:
            if num == f:
                c1 += 1
            elif num == s:
                c2 += 1
            elif c1 == 0:
                f = num
                c1 = 1
            elif c2 == 0:
                s = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        
        threshold = len(nums) // 3
        result = []
        
        for candidate in set([f, s]):
            if candidate is not None and nums.count(candidate) > threshold:
                result.append(candidate) 
        return result