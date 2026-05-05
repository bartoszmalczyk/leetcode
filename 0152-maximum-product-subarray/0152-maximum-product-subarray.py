class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 
        res = max(nums)
        cur_max = cur_min = 1
        
        for n in nums:
            temp = cur_max * n
            cur_max = max(temp, cur_min * n, n)
            cur_min = min(temp, cur_min * n, n)

            res = max(res, cur_max)
        return res
        




