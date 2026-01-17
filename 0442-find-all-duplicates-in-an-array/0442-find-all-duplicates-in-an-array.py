from collections import defaultdict
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hm = defaultdict(int)
        ans = []
        for i in nums:
            hm[i] += 1
            if hm[i] == 2:
                ans.append(i)
        return ans