class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m = min(nums)
        ans = 0
        for i in nums:
            ans += i - m
        return ans
