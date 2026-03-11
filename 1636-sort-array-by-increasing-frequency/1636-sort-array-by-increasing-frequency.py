from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        temp = Counter(nums)
        nums.sort(key = lambda x: (temp[x], -x))
        return nums
        