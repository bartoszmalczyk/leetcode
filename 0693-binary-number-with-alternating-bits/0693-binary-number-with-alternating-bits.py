class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n != 1:
            f = n & 1
            print(f)
            n = n >> 1 
            print(n)
            s = n & 1
            print(s)
            if f == s: return False
        return True
