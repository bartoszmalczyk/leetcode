class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans = []
        for index, num in enumerate(nums):
            if num == target:
                ans.append(index)
        return ans