from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        hm = defaultdict(int)
        for i in s:
            hm[i] += 1
        hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse = True))
        ans = ""
        for key in list(hm.keys()):
            for x in range(hm[key]):
                ans += key
        return ans