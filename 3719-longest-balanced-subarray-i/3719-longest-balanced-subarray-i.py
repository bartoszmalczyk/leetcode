class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = float('-inf')
        for i in range(len(nums)):
            odd = set()
            even = set()

            for j in range(i, len(nums)):
                if nums[j] % 2 != 0: 
                    odd.add(nums[j])
                else:
                    even.add(nums[j])
                if len(odd) == len(even):
                    ans = max(ans, j - i + 1)
        if ans < 0: return 0 
        return ans