class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        mod = len(nums)
        ans = []
        for i in range(mod):
            ans.append(nums[(i + nums[i]) % mod])
        return ans
