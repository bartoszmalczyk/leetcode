from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hm = defaultdict(int)
        l = 0 
        ans = 0
        for r in range(len(s)):
            hm[s[r]] += 1
            while hm[s[r]] > 2:
                hm[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans

           
