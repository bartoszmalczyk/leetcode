from collections import Counter
from math import ceil
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        hm = Counter(arr)
        n = len(arr)
        threshold = 0.25 * n
        for key in hm:
            if hm[key] > threshold:
                return key
