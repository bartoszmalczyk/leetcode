from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hm = defaultdict(list)
        min_ = float('inf')
        for i in range(len(nums)):
            hm[nums[i]].append(i)

        for candidate in list(hm.values()):
            if len(candidate) < 3: continue
            for m in range(len(candidate)-2):
                i = candidate[m]
                j = candidate[m+1]
                k = candidate[m+2]
                min_ = min(min_, abs(i - j) + abs(j - k) + abs(k - i))
        if min_ == float('inf'):
            return -1 
        return min_

        