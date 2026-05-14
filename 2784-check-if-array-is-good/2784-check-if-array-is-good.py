from collections import defaultdict 
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        ones_counter = 0 
        two_counter = 0
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        print(hm)
        for i in range(1, len(nums) - 1):
            if hm[i] != 1:
                return False
        if hm[len(nums) - 1] == 2:
            return True
        else:
            return False

        
        

