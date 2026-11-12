class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev1 = nums[0]
        prev2 = nums[0]
        longest_streak = 0 
        temp1 = 1
        temp2 = 1 
        for i in range(1, len(nums)):
            if nums[i] > prev1: 
                temp1 += 1
                prev1 = nums[i]
            else:
                longest_streak = max(longest_streak, temp1)
                temp1 = 1
                prev1 = nums[i]

            if nums[i] < prev2:
                temp2 += 1
                prev2 = nums[i]
            else:
                longest_streak = max(longest_streak, temp2)
                temp2 = 1
                prev2 = nums[i]

        return max(longest_streak, temp1, temp2)