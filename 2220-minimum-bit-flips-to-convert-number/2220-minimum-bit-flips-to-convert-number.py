import math
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # 10 1010
        # 7  0111
        ans = start ^ goal 
        return ans.bit_count()
