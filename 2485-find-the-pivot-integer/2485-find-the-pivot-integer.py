class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1: return 1 
        first = 0 
        second = (1+n) / 2 * n 
        for i in range(1,n):
            first += i 
            second -= (i - 1)
            if first == second:
                return i            
        return -1