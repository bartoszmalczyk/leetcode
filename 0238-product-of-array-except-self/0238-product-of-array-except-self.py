class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        sub = [1] * n 

        # pre & sub populate 
        for i in range(1,n):
            pre[i] = pre[i - 1] * nums[i - 1]
            sub[n - 1 - i] = sub[n - i] * nums[n - i]
        
        ans = [pre[k] * sub[k] for k in range(n)]
        return ans

