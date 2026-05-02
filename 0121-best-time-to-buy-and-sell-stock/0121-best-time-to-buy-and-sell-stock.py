class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0 
        min_ = float('inf')

        for p in prices:
            min_ = min(min_, p)
            best = max(p - min_, best)
        return best
