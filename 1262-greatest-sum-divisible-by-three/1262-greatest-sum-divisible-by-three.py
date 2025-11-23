class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        if total % 3 == 0:
            return total 
        else:
            mod1 = sorted([x for x in nums if x % 3 == 1])
            mod2 = sorted([x for x in nums if x % 3 == 2])
            reminder = total % 3 
            
            to_remove = 1001
            if reminder == 1:
                if mod1: 
                    to_remove = min(mod1[0], to_remove)
                if len(mod2) >= 2:
                    to_remove = min(mod2[0] + mod2[1], to_remove)
            else:
                if mod2: 
                    to_remove = min(mod2[0], to_remove)
                if len(mod1) >= 2:
                    to_remove = min(mod1[0] + mod1[1], to_remove)
            return total - to_remove

                

