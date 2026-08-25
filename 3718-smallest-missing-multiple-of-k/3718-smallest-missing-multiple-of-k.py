class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        temp = set(nums)
        m = 1
        while True:
            if k * m not in temp:
                return k * m 
            else: 
                m += 1 