from collections import defaultdict
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
            if hm[num] >= 2:
                return num
