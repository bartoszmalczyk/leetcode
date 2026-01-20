from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
            else:
                for j in range(x):
                    if (j | (j + 1)) == x:
                        ans.append(j)
                        break 
        return ans