class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mn = [-1, float('inf')] # index value
        mx = [-1, float('-inf')]
        for i, v in enumerate(nums):
            if v < mn[1]:
                mn = [i, v]
            if v > mx[1]:
                mx = [i, v]
        mx_i = mx[0]    
        mn_i = mn[0]
        
        n = len(nums)
        
        f1 = False
        f2 = False 
        for i in range(n - 1):
            if not (nums[(mx_i + i) % n] > nums[(mx_i + i + 1) % n]) and not f1:
                f1 = True
            if not (nums[(mn_i + i) % n] < nums[(mn_i + i + 1) % n]) and not f2:
                f2 = True 
                
        if f1 and f2: 
            return -1
            
        ans = float('inf')
        if not f2:
            ans = min(ans, mn_i, (n - mn_i) % n + 2)
        if not f1:
            ans = min(ans, mx_i + 1, n - mn_i)
            
        return ans