from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_c = Counter(s)
        t_c = Counter(t)
        return (t_c - s_c).most_common()[0][0]


            

