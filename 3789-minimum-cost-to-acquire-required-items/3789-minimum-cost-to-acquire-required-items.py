class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:  
        cost = min(costBoth, cost1 + cost2) * min(need1, need2)
        if need1 >= need2: 
            cost += (need1 - need2) * min(costBoth, cost1)
        else: 
            cost += (need2 - need1) * min(costBoth, cost2)
        return cost
        
