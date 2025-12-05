from typing import List
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n-1):
            diff = sum(nums[0:i+1]) - sum(nums[i+1:n])
            if diff % 2 == 0:
                ans+=1
            else:
                continue
        return ans