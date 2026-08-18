from collections import defaultdict
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)

        for j in range(0, len(nums) - k + 1):
            temp = set(nums[j:j + k])
            for i in temp:
                counter[i] += 1
        potential = []
        for k, v in counter.items():
            if v == 1:
                potential.append(k)
        return -1 if not potential else max(potential)





