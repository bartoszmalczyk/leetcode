class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        increasing = (nums[0] < nums[-1])
        for i in range(0,len(nums) - 1):
            if increasing: 
                if nums[i+1] < nums[i]:
                    return False
            else:
                if nums[i+1] > nums[i]:
                    return False
        return True