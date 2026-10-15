class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        temp = set()
        for i in range(n):
            temp.clear()
            for j in range(i, n):
                temp.add(nums[j])
                ans += len(temp) * len(temp)
        return ans
