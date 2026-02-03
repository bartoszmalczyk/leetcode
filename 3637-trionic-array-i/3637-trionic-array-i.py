class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        i = 0 
        res = [False, False, False]
        while i + 1 < n and nums[i] < nums[i+1]:
            res[0] = True
            i += 1
        while i + 1 < n and nums[i] > nums[i+1]:
            res[1] = True
            i += 1
        while i + 1 < n and nums[i] < nums[i+1]:
            res[2] = True
            i += 1
    
        return i == n - 1 and res[0] and res[1] and res[2]

    