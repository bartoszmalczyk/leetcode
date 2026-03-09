class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            left = target - num
            if left in hashmap:
                return [hm[left], i]
            hm[num] = i
        