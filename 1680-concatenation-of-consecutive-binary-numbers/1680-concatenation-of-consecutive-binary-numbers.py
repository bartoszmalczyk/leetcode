class Solution:
    def concatenatedBinary(self, n: int) -> int:
        #n = 3, 1 = 1, 2 = 10, 3 = 11   1 + 10 + 11 = 11011 
        ans = ""
        MOD = 10**9 + 7
        for i in range(1, n + 1):
            ans += format(i, 'b')
        return int(ans, 2) % MOD