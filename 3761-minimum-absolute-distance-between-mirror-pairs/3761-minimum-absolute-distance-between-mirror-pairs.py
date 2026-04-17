from collections import defaultdict
from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        hm = defaultdict(lambda: -1)
        min_ = float('inf')
        for index, num in enumerate(nums):
            if hm[num] != -1:
                min_ = min(min_, index - hm[num])
            mirror = int(str(num)[::-1])
            hm[mirror] = index
        return -1 if min_ == float('inf') else min_