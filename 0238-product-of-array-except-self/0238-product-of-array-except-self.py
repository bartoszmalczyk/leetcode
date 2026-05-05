class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        sub = [1] * n 

        # pre populate 
        for i in range(1,n):
            pre[i] = pre[i - 1] * nums[i - 1]
        
        # sub populate 
        for j in range(n - 2, -1, -1):
            sub[j] = sub[j + 1] * nums[j + 1]
        
        ans = [pre[k] * sub[k] for k in range(n)]
        return ans


"""
nums [1,2,3,4]
pre = [1, 1, 2, 6]
sub = [24, 12, 4, 1]

"""