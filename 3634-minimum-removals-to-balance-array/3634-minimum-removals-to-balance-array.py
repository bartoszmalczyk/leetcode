class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)   
        i, max_l = 0, 0
        nums.sort()
        for j in range(len(nums)):
            while nums[j] > nums[i] * k:
                i += 1
            max_l = max(max_l, j - i + 1)
            
        return n - (max_l)

