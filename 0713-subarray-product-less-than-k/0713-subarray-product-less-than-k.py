
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # [2, 5, 6, 10]
        if k <= 1: return 0 
        ans = 0
        l, r = 0, 0
        product = 1 
        while r < len(nums):
            product *= nums[r]
            while product >= k:
                product //= nums[l]
                l += 1
            ans += (r - l) + 1
            r += 1
        return ans
            
