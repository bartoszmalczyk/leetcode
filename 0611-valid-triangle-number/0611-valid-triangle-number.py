class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        for temp in range(n - 1, 1, -1):
            l = 0 
            r = temp - 1
            while l < r:
                if nums[l] + nums[r] > nums[temp]:
                    ans += (r - l)
                    r -= 1
                elif nums[l] + nums[r] <= nums[temp]:
                    l += 1
        return ans

