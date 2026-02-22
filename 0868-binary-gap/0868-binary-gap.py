class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        last_one_index = None
        counter = 0
        while n > 0:
            if n & 1 == 1:
                if last_one_index is not None: 
                    ans = max(ans, counter - last_one_index)
                last_one_index = counter
            counter += 1
            n >>= 1
        return ans

            