import math
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal 
        return ans.bit_count()

