class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(len(nums) - 2):
            l = i + 1
            r = n - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp < 0:
                    l += 1
                elif temp > 0:
                    r -= 1
                else:
                    ans.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1 
                    r -= 1
        return list(ans)