class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        temp = 0
        ans = 0
        hm = {0: -1} 

        for i in range(len(nums)):
            curr = nums[i]
            temp += -1 if curr == 0 else 1
            
            if temp in hm:
                ans = max(ans, i - hm[temp])
            else:
                hm[temp] = i 
            
        return ans