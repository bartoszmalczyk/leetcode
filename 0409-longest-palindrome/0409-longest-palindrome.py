from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = defaultdict(int)
        for i in s:
            hm[i] += 1
        has_odd = False
        ans = 0
        for i in list(hm.values()):
            if i % 2 != 0:
                has_odd = True
                ans += i - 1
            else: 
                ans += i
        if has_odd: 
            return ans + 1
        else: return ans
    
    