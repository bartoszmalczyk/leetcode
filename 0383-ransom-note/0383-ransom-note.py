from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm_a = defaultdict(int)
        hm_b = defaultdict(int)
        for i in ransomNote:
            hm_a[i] += 1
        for i in magazine:
            hm_b[i] += 1
        for symbol in hm_a:
            if hm_a[symbol] > hm_b[symbol]:
                return False
        return True
        