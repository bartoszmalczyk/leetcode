class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        fMin = float('inf')
        sMin = float('inf')

        for i in range(1, len(nums)):
            if nums[i] < fMin:
                sMin = fMin
                fMin = nums[i]
            elif nums[i] < sMin:
                sMin = nums[i]

        return nums[0] + fMin + sMin

