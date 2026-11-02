class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = None
        n = len(nums)
        if n % 2 == 0:
            median = (nums[n // 2] + nums[n // 2 -  1]) // 2
        else:
            median = nums[n//2]

        ans = 0 
        for num in nums:
            print(num - median)
            ans += abs(num - median)
        return ans

