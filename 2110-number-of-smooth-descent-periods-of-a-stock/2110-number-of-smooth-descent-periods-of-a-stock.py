class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if len(prices) == 1: return 1 
        ans = 0        
        period = []
        streak = 1
        for i in range(len(prices)-1):
            if prices[i] - prices[i+1] == 1:
                streak += 1
            else:
                ans += streak * (streak + 1) // 2 
                streak = 1
        ans += streak * (streak + 1) // 2 
            
        return ans 