class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maximum = [nums[0]] 
        minimum = [nums[-1]]
        n = len(nums)
        for i in range(1, len(nums)):
            maximum.append(max(maximum[-1], nums[i]))
            minimum.append(min(minimum[-1], nums[n - i - 1]))
        minimum = minimum[::-1]

        for i in range(n):
            temp = maximum[i] - minimum[i]
            if temp <= k:
                return i 
        return -1