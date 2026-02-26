class Solution:
    def numSteps(self, s: str) -> int:
        s = int(s, 2)
        counter = 0 
        while s != 1:
            if (s & 1) == 0: 
                s = s // 2
            else: 
                s += 1
            counter += 1
        return counter