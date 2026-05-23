class Solution:
    def check(self, nums: List[int]) -> bool:
        changes = 0
        for i in range(len(nums)):
            if not nums[i] <= nums[(i + 1) % len(nums)]:
                changes += 1
            if changes > 1:
                return False
        return True