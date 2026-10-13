class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ans = 0
        nums = sorted(nums, key=abs)
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            ans -= nums[l] * nums[l]
            ans += nums[r] * nums[r]
            r -= 1
            l += 1
        if n % 2 != 0:
            ans += nums[n // 2] * nums[n // 2]
        return ans


