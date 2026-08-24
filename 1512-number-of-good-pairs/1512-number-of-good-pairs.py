from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        x = Counter(nums)
        ans = 0
        for v in x.values():
            ans += (v * (v - 1)//2)
        return ans