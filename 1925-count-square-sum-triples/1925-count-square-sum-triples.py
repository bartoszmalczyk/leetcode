import math

class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0 
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                val = i ** 2 + j ** 2
                c_sqrt = math.sqrt(val)
                if c_sqrt.is_integer() and c_sqrt <= n:
                    ans += 1

        return ans
