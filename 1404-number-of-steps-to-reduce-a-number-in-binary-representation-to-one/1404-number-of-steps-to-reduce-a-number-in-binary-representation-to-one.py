class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s, 2)
        counter = 0 
        while n != 1:
            if (n & 1) == 0: 
                n = n // 2
            else: 
                n += 1
            counter += 1
        return counter