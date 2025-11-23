class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        remainder = total % 3
        if remainder == 0:
            return total
        rem1 = sorted([x for x in nums if x % 3 == 1])
        rem2 = sorted([x for x in nums if x % 3 == 2])
        to_remove = float('inf')
        if remainder == 1:
            if rem1:
                to_remove = min(to_remove, rem1[0])
            if len(rem2) >= 2:
                to_remove = min(to_remove, rem2[0] + rem2[1])
                
        elif remainder == 2:
            if rem2:
                to_remove = min(to_remove, rem2[0])
            if len(rem1) >= 2:
                to_remove = min(to_remove, rem1[0] + rem1[1])

        return total - to_remove