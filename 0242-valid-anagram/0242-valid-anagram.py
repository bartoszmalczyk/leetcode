from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        
        hm_s = defaultdict(int)
        hm_t = defaultdict(int)

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            hm_s[s_char] += 1
            hm_t[t_char] += 1
        return hm_s == hm_t

        
        