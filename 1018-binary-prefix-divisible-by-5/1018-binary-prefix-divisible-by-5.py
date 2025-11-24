class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = 0
        ans = []
        for i in nums:
            n = 2 * n + i
            if n % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans