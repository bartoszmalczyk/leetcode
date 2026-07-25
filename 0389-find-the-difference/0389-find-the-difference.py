from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_c = Counter(s)
        t_c = Counter(t)
        return next(iter(t_c - s_c))


            

