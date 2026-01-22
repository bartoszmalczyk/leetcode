class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if nums == sorted(nums):
            return 0
        nums = list(nums)
        steps = 0
        while nums != sorted(nums):
            mn = float('inf')
            pos = -1
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if current_sum < mn:
                    mn = current_sum
                    pos = i
            if pos != -1:
                nums[pos] = mn     
                nums.pop(pos + 1)   
                steps += 1          
            else:
                break 
        return steps