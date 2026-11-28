class Solution:
    def canAliceWin(self, n: int) -> bool:
        curr = 10 
        counter = 0 
        while n >= curr: 
            n -= curr
            curr -= 1
            counter += 1
        return counter % 2 == 1
            