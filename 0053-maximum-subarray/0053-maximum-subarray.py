class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 
        curr_sum = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            ans = max(ans, curr_sum)
        return ans

