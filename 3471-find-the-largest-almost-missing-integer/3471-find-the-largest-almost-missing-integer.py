from collections import defaultdict
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)

        for j in range(0, len(nums) - k + 1):
            temp = set(nums[j:j + k])
            for i in temp:
                counter[i] += 1
        max_ = -1
        for k, v in counter.items():
            if v == 1:
                max_ = max(max_, k)
        return max_





