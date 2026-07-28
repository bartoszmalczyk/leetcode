import heapq
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        max_heap = [-x for x in unique_nums]
        if len(unique_nums) < 3:
            return max(unique_nums)
        heapq.heapify(max_heap)
        heapq.heappop(max_heap)
        heapq.heappop(max_heap)
        return -heapq.heappop(max_heap)