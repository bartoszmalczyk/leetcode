class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        set_nums = set(nums)
        while True:
            if original in set_nums:
                original *= 2
            else: return original
        