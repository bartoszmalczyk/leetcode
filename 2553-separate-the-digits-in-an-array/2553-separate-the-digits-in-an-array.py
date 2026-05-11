class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num < 10:
                ans.append(num)
            else:
                for c in str(num):
                    ans.append(int(c))
        return ans
