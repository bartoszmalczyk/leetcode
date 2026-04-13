class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if nums[start] == target: return 0
        for i in range(len(nums)):
            if start - i >= 0:
                left = start - i
                if nums[left] == target: return abs(left - start)
            if start + i < len(nums):
                right = start + i
                if nums[right] == target: return abs(right - start)