from collections import Counter
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = [] 
        hm1 = Counter(digits)
        for i in range(100,1000, 2):
            temp = []
            for x in str(i):
                temp.append(int(x))
            hm2 = Counter(temp)
            if not hm2 - hm1:
                ans.append(i)
        return len(ans)
                        