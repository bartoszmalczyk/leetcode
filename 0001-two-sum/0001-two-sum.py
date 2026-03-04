class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            left = target - num
            if left in hm:
                return [hm[left], i]
            hm[left] = i
        