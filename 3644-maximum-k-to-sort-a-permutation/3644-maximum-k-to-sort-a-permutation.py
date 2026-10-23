class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        ans = None
        for i in range(len(nums_sorted)):
            if nums_sorted[i] != nums[i]:
                if ans is None:
                    ans = nums[i]
                else:
                    ans &= nums[i]
        return ans if ans else 0