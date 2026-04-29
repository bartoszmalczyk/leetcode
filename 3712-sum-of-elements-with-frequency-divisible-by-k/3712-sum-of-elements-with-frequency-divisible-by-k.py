from collections import defaultdict
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        ans = 0
        for num in nums:
            hm[num] += 1
        
        for key, value in hm.items():
            if value % k == 0:
                ans += (key * value)
        
        return ans
