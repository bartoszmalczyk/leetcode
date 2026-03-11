from collections import defaultdict
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        temp = list(hm.items())
        temp = sorted(temp, key = lambda x: (x[1], -x[0]))
        ans = []
        for char, apperance in temp:
            for _ in range(apperance):
                ans.append(char)
        return ans
        