class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a