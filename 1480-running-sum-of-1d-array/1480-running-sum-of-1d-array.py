class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        dp = [nums[0]]
        for i in range(1,len(nums)):
            dp.append(dp[-1] + nums[i])
        return dp