class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        remainder = total % 3
        if remainder == 0:
            return total
        mod1 = sorted([x for x in nums if x % 3 == 1])
        mod2 = sorted([x for x in nums if x % 3 == 2])
        to_remove = float('inf')

        if remainder == 1:
            if mod1:
                to_remove = min(to_remove, mod1[0])
            if len(rem2) >= 2:
                to_remove = min(to_remove, mod2[0] + mod2[1])

        elif remainder == 2:
            if mod2:
                to_remove = min(to_remove, mod2[0])
            if len(mod1) >= 2:
                to_remove = min(to_remove, mod1[0] + mod1[1])
        return total - to_remove