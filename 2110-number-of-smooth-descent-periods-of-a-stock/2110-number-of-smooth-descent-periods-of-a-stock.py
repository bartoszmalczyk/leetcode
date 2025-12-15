class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if len(prices) == 1: return 1 
        
        period = []
        streak = 1
        for i in range(len(prices)-1):
            if prices[i] - prices[i+1] == 1:
                streak += 1
            else:
                period.append(streak)
                streak = 1
        period.append(streak) 
            
        ans = 0
        for i in period:
            ans += i * (i + 1) // 2 
        return ans 