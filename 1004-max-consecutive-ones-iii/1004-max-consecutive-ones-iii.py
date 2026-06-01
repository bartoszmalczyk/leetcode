class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        l = 0 
        r = 0
        n = len(nums)
        ans = 0
        while r <= n - 1:
            
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans 