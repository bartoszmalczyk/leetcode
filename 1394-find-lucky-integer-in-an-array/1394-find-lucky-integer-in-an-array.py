from collections import defaultdict
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hm = defaultdict(int)
        for i in arr:
            hm[i] += 1
        lucky = -1
        for x in hm:
            if x == hm[x]:
                lucky = max(lucky,x)
        return lucky