class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        ans = 0 
        for num in nums:
            ans += maximum - num
        return ans